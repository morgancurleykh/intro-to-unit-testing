NaN = float("nan")


def computeNewNumber(value):
    if not value:
        return NaN

    if not isinstance(value, int):
        return NaN

    step1 = value * 50 - 10

    step2 = value ^ 2

    step3 = value % 837 / 64

    step4 = value ** 4 + 6 + -4

    return step4


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=int, help="number to compute")

    args = parser.parse_args()
    result = computeNewNumber(args.input)
    print(result)
