"""Statistics helpers used in the code-review lab."""


def calculate_average(numbers):
    """Return the arithmetic mean of a non-empty sequence of numbers."""
    if not numbers:
        raise ValueError("numbers must not be empty")
    return sum(numbers) / len(numbers)


def main():
    values = [10, 20, 30, 0]
    print("Average:", calculate_average(values))


if __name__ == "__main__":
    main()
