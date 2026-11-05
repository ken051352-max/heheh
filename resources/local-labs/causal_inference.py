"""CPU-only causal identification lab; synthetic data, standard library only."""
import argparse
import json
import math
import random
from statistics import NormalDist, mean, variance

TRUE_EFFECT = 2.0


def generate(n, seed, randomized, noise=1.0):
    """Y(0)=3X+epsilon, Y(1)=Y(0)+2; target P(X=1)=1/2."""
    if n < 40 or n % 2:
        raise ValueError("n must be even and at least 40")
    rng = random.Random(seed)
    rows = []
    for i in range(n):
        x = i % 2
        propensity = 0.5 if randomized else (0.8 if x else 0.2)
        treatment = int(rng.random() < propensity)
        y0 = 3 * x + rng.gauss(0, noise)
        rows.append((x, treatment, y0 + TRUE_EFFECT * treatment))
    return rows


def difference(rows):
    treated = [y for _, t, y in rows if t]
    control = [y for _, t, y in rows if not t]
    if min(len(treated), len(control)) < 2:
        raise ValueError("Insufficient treated/control observations: inspect overlap")
    estimate = mean(treated) - mean(control)
    se = math.sqrt(variance(treated) / len(treated) + variance(control) / len(control))
    return estimate, se


def adjusted(rows):
    """Standardize conditional contrasts to the known 50/50 target population."""
    by_x = [difference([r for r in rows if r[0] == x]) for x in (0, 1)]
    return sum(e for e, _ in by_x) / 2, math.sqrt(sum(se**2 for _, se in by_x)) / 2


def sample_size_per_arm(sigma, mde, alpha=0.05, power=0.8):
    """Normal approximation: equal independent arms, known common variance."""
    if not math.isfinite(sigma) or not math.isfinite(mde) or sigma <= 0 or mde <= 0 or not 0 < alpha < 1 or not 0.5 < power < 1:
        raise ValueError("Invalid prospective design parameters")
    normal = NormalDist()
    z = normal.inv_cdf(1 - alpha / 2) + normal.inv_cdf(power)
    return math.ceil(2 * sigma**2 * z**2 / mde**2)


def run(n=800, trials=200, seed=42):
    if trials < 20:
        raise ValueError("Use at least 20 repetitions; inspect Monte Carlo error")
    experiments = {"randomized": [], "confounded_naive": [], "confounded_adjusted": []}
    for i in range(trials):
        randomized = generate(n, seed + 2 * i, True)
        confounded = generate(n, seed + 2 * i + 1, False)
        experiments["randomized"].append(difference(randomized))
        experiments["confounded_naive"].append(difference(confounded))
        experiments["confounded_adjusted"].append(adjusted(confounded))
    report = {"truth": TRUE_EFFECT, "n": n, "trials": trials, "seed": seed}
    for name, estimates in experiments.items():
        coverage = mean(abs(e - TRUE_EFFECT) <= 1.96 * se for e, se in estimates)
        report[name] = {
            "mean_estimate": mean(e for e, _ in estimates),
            "bias": mean(e - TRUE_EFFECT for e, _ in estimates),
            "coverage_approx_95pct": coverage,
            "coverage_monte_carlo_se": math.sqrt(coverage * (1 - coverage) / trials),
        }
    report["design"] = {
        "mde": 0.3, "sigma": math.sqrt(3.25), "alpha": 0.05, "power": 0.8,
        "n_per_arm_normal_approx": sample_size_per_arm(math.sqrt(3.25), 0.3),
    }
    # Exact identification check: within-X contrast equals the known effect without noise.
    exact = adjusted(generate(n, seed, False, noise=0))[0]
    assert math.isclose(exact, TRUE_EFFECT, abs_tol=1e-12)
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=800)
    parser.add_argument("--trials", type=int, default=200)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    print(json.dumps(run(args.n, args.trials, args.seed), indent=2))
