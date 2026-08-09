OPERATIONS = {
    "+": (lambda left, right: left + right, "sum"),
    "-": (lambda left, right: left - right, "difference"),
    "*": (lambda left, right: left * right, "product"),
    "/": (lambda left, right: left / right, "quotient"),
}


def calculate(left, operator, right):
    """Return the result for a supported operation."""
    if operator not in OPERATIONS:
        raise ValueError("Unsupported operation. Choose +, -, *, or /.")
    if operator == "/" and right == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return OPERATIONS[operator][0](left, right)


def main():
    try:
        left = float(input("Enter the first number: "))
        right = float(input("Enter the second number: "))
        operator = input("Choose an operation (+, -, *, /): ").strip()
        result = calculate(left, operator, right)
        label = OPERATIONS[operator][1]
        print(f"The {label} of {left:g} and {right:g} is: {result:g}")
    except ValueError as error:
        print(error)
    except ZeroDivisionError as error:
        print(error)


if __name__ == "__main__":
    main()