def add(a: int, b: int) -> int:
    return a + b


def main() -> None:
    num1 = int(input("Enter The Number :: "))
    num2 = int(input("Enter The Number :: "))

    result = add(num1, num2)
    print("Sum of two Numbers is :: ", result)


if __name__ == "__main__":

    main()