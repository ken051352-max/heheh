import pytest


@pytest.mark.parametrize("left,operator,right,expected", [
    ("2", "+", "3", 5), ("2", "-", "5", -3),
    ("2.5", "*", "4", 10), ("7", "/", "2", 3.5),
    ("-4", "+", " 2 ", -2), ("0", "/", "4", 0),
])
def test_arithmetic(project, left, operator, right, expected):
    assert project("calculator").calculate(left, operator, right) == pytest.approx(expected)


@pytest.mark.parametrize("left,operator,right", [
    ("hello", "+", "3"), ("", "+", "2"), ("1", "/", "0"),
    ("1", "/", "-0.0"), ("2", "**", "3"), ("NaN", "+", "1"),
    ("1", "+", "inf"), ("1e308", "*", "1e308"),
])
def test_rejects_bad_input_or_unrepresentable_result(project, left, operator, right):
    with pytest.raises(ValueError):
        project("calculator").calculate(left, operator, right)


def test_cli_exit_codes_and_streams(project, capsys):
    calculator = project("calculator")
    assert calculator.main(["2", "+", "3"]) == 0
    assert float(capsys.readouterr().out) == 5
    assert calculator.main(["1", "/", "0"]) != 0
    output = capsys.readouterr()
    assert output.err and not output.out
