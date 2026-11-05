"""Your M1 starter. Implement calculate; keep input/output at the edge."""
import argparse
import sys


def calculate(left: str, operator: str, right: str) -> float:
    """Accept finite numbers and +, -, *, /. Raise ValueError for invalid work.

    TODO: convert operands, reject non-finite values, choose the operation,
    handle zero division, and reject a non-finite result. Do not use eval().
    """
    raise NotImplementedError("Implement calculate after CS50P Lecture 3")


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
