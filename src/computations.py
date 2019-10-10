NaN = float("nan")


def step_1(i):
    return i * 50 - 10


def step_2(i):
    return i ^ 2


def step_3(i):
    return i % 837 / 64


def step_4(i):
    return i ** 4 + 6 + -4


def computeNewNumber(value):
    if not isinstance(value, int):
        return NaN

    step1 = step_1(value)

    step2 = step_2(step1)

    step3 = step_3(step2)

    step4 = step_4(step3)

    return step4


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=int, help="number to compute")

    args = parser.parse_args()
    result = computeNewNumber(args.input)
    print(result)
