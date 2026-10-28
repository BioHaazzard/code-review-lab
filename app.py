"""Simple statistics helpers used in the code-review lab."""

import os


def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total / len(numbers)


def main():
    values = [10, 20, 30, 0]
    print("Average:", calculate_average(values))


if __name__ == "__main__":
    main()
