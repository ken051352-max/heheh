import json
from pathlib import Path
from unittest.mock import MagicMock, Mock
from urllib.error import HTTPError, URLError
import pytest

FIXTURES = Path(__file__).parents[1] / "weather" / "fixtures"
RAW = (FIXTURES / "current.json").read_bytes()


def test_temperature_and_timestamp_preserved(project):
    assert project("weather").parse_weather(RAW) == {
        "temperature_c": 12.5, "observed_at_utc": "2026-01-01T09:00"}


@pytest.mark.parametrize("raw", [
    (FIXTURES / "malformed.json").read_bytes(),
    (FIXTURES / "missing-temperature.json").read_bytes(),
    b"null", b"[]", b"\xff", RAW.decode("utf-8").encode("utf-16"),
])
def test_invalid_payloads(project, raw):
    weather = project("weather")
    with pytest.raises(weather.WeatherError):
        weather.parse_weather(raw)


@pytest.mark.parametrize("replacement", [None, True, "12.5", float("nan"), float("inf")])
def test_temperature_must_be_finite_number(project, replacement):
    weather = project("weather")
    data = json.loads(RAW)
    data["current"]["temperature_2m"] = replacement
    with pytest.raises(weather.WeatherError):
        weather.parse_weather(json.dumps(data).encode())


def test_units_and_timestamp_checked(project):
    weather = project("weather")
    for field, value in (("units", "°F"), ("time", "yesterday"),
                         ("time", "2026-01-01T09:00+05:30")):
        data = json.loads(RAW)
        if field == "units":
            data["current_units"]["temperature_2m"] = value
        else:
            data["current"]["time"] = value
        with pytest.raises(weather.WeatherError):
            weather.parse_weather(json.dumps(data).encode())


def test_offline_never_fetches_or_writes_cache(project, tmp_path):
    weather = project("weather")
    fetch = Mock(side_effect=AssertionError("network attempted"))
    cache = tmp_path / "cache.json"
    result = weather.get_weather(" Delhi ", cache, fetch=fetch)
    assert result["source"] == "synthetic fixture" and result["city"] == "delhi"
    fetch.assert_not_called()
    assert not cache.exists()


def test_unknown_city_and_missing_fixture_fail_usefully(project, tmp_path):
    weather = project("weather")
    fetch = Mock()
    with pytest.raises(weather.WeatherError):
        weather.get_weather("Atlantis", tmp_path / "cache", fetch=fetch)
    fetch.assert_not_called()
    with pytest.raises(weather.WeatherError):
        weather.get_weather("Delhi", tmp_path / "cache", fixture=tmp_path / "missing")


def test_live_adapter_request_and_cache_reuse(project, tmp_path):
    weather = project("weather")
    fetch = Mock(return_value=RAW)
    cache = tmp_path / "cache.json"
    first = weather.get_weather("London", cache, offline=False, fetch=fetch, now=100, timeout=3)
    second = weather.get_weather("London", cache, offline=False, fetch=fetch, now=109, ttl=10)
    assert first["source"] == "provider" and second["source"] == "cache"
    assert first["temperature_c"] == second["temperature_c"] == 12.5
    fetch.assert_called_once()
    url, timeout = fetch.call_args.args
    assert "timezone=UTC" in url and "temperature_2m" in url and timeout == 3


def test_cache_exact_expiry_future_time_and_city_are_misses(project, tmp_path):
    weather = project("weather")
    cache = tmp_path / "cache.json"
    weather.write_cache(cache, "delhi", RAW, 100)
    assert weather.read_cache(cache, "delhi", 109, 10) is not None
    assert weather.read_cache(cache, "delhi", 110, 10) is None
    assert weather.read_cache(cache, "delhi", 99, 10) is None
    assert weather.read_cache(cache, "london", 101, 10) is None


def test_corrupt_cache_is_refreshed(project, tmp_path):
    weather = project("weather")
    cache = tmp_path / "cache.json"
    cache.write_text("{broken", encoding="utf-8")
    fetch = Mock(return_value=RAW)
    assert weather.get_weather("Delhi", cache, offline=False, fetch=fetch, now=100)["source"] == "provider"
    fetch.assert_called_once()


@pytest.mark.parametrize("failure", [
    TimeoutError("socket timeout"), URLError("offline"),
    HTTPError("https://fixture.invalid", 429, "rate limited", {}, None),
    HTTPError("https://fixture.invalid", 503, "unavailable", {}, None),
])
def test_failed_requests_do_not_write_or_retry(project, tmp_path, failure):
    weather = project("weather")
    cache = tmp_path / "cache.json"
    fetch = Mock(side_effect=failure)
    with pytest.raises(weather.WeatherError):
        weather.get_weather("Delhi", cache, offline=False, fetch=fetch, now=100)
    fetch.assert_called_once()
    assert not cache.exists()


def test_malformed_response_is_not_cached(project, tmp_path):
    weather = project("weather")
    cache = tmp_path / "cache.json"
    with pytest.raises(weather.WeatherError):
        weather.get_weather("Delhi", cache, offline=False, fetch=lambda *_: b"null", now=100)
    assert not cache.exists()


def test_unwritable_cache_preserves_prior_file(project, tmp_path, monkeypatch):
    weather = project("weather")
    cache = tmp_path / "cache.json"
    cache.write_text("prior", encoding="utf-8")
    monkeypatch.setattr(weather.tempfile, "NamedTemporaryFile", Mock(side_effect=PermissionError("fixture")))
    with pytest.raises(weather.WeatherError):
        weather.write_cache(cache, "delhi", RAW, 100)
    assert cache.read_text(encoding="utf-8") == "prior"


def test_failed_cache_replacement_preserves_prior_and_cleans_temp(project, tmp_path, monkeypatch):
    weather = project("weather")
    cache = tmp_path / "cache.json"
    cache.write_text("prior", encoding="utf-8")
    monkeypatch.setattr(weather.Path, "replace", Mock(side_effect=PermissionError("fixture")))
    with pytest.raises(weather.WeatherError):
        weather.write_cache(cache, "delhi", RAW, 100)
    assert cache.read_text(encoding="utf-8") == "prior"
    assert list(tmp_path.glob(".weather-*.tmp")) == []


@pytest.mark.parametrize("parameter", ["ttl", "timeout"])
@pytest.mark.parametrize("value", [0, -1, float("inf"), True, "5"])
def test_invalid_config_rejected_before_request(project, tmp_path, parameter, value):
    weather = project("weather")
    fetch = Mock()
    with pytest.raises(weather.WeatherError):
        weather.get_weather("Delhi", tmp_path / "cache", offline=False, fetch=fetch,
                            **{parameter: value})
    fetch.assert_not_called()


@pytest.mark.parametrize("size", [65_536, 65_537])
def test_download_bounds_response_and_forwards_timeout(project, monkeypatch, size):
    weather = project("weather")
    response = MagicMock()
    response.__enter__.return_value = response
    response.read.return_value = b"x" * size
    opener = Mock(return_value=response)
    monkeypatch.setattr(weather, "urlopen", opener)
    if size == 65_536:
        assert weather.download("https://fixture.invalid/weather", 2) == b"x" * size
    else:
        with pytest.raises(weather.WeatherError):
            weather.download("https://fixture.invalid/weather", 2)
    opener.assert_called_once_with("https://fixture.invalid/weather", timeout=2)
    response.read.assert_called_once_with(65_537)
    response.__exit__.assert_called_once()


def test_cli_reports_failure_without_success_output(project, capsys):
    assert project("weather").main(["Atlantis", "--offline"]) != 0
    output = capsys.readouterr()
    assert output.err and not output.out
