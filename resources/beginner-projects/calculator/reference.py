"""Worked example for reviewers. Attempt starter.py before reading this."""
import argparse
import math
import sys


def calculate(left: str, operator: str, right: str) -> float:
    try:
        a, b = float(left), float(right)
    except (ValueError, TypeError) as error:
        raise ValueError("enter two numbers") from error
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("numbers must be finite")
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b == 0:
            raise ValueError("the divisor must not be zero")
        result = a / b
    else:
        raise ValueError("choose +, -, *, or /")
    if not math.isfinite(result):
        raise ValueError("result is outside the finite float range")
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description="One calculation, with useful errors.")
    parser.add_argument("left")
    parser.add_argument("operator")
    parser.add_argument("right")
    args = parser.parse_args(argv)
    try:
        print(calculate(args.left, args.operator, args.right))
    except ValueError as error:
        print(f"Cannot calculate: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
