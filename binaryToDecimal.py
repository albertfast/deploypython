def bin_to_dec(s):
    """
    Convert a binary number string to a decimal number.

    Args:
    s (str): A string representing a binary number, between 1 - 10 characters.

    Returns:
    int: An integer that represents the decimal representation.
    """
    if not s.strip():
        raise ValueError("Input cannot be empty.")

    if not all(char in '01' for char in s):
        raise ValueError("Input must be a binary number containing only 0s and 1s.")

    if len(s) > 10 or len(s) < 1:
        raise ValueError("Input must be a binary string between 1 and 10 characters long.")

    decimal_number = 0
    detailed_steps = []
    length = len(s)

    for index, bit in enumerate(s):
        power_of_two = length - 1 - index
        contribution = int(bit) * (2 ** power_of_two)
        detailed_steps.append(f"2^{power_of_two} * {bit} = {contribution}")
        decimal_number += contribution

    detailed_explanation = " + ".join(detailed_steps)
    print(f"The computation steps for binary {s} are:\n" + "\n".join(detailed_steps))
    print(f"\nDetailed computation: {detailed_explanation}")

    return decimal_number


def main():
    binary_string = input("Enter a binary number string (1-10 characters): ").strip()
    try:
        decimal_number = bin_to_dec(binary_string)
        print(f"The decimal representation of the binary number '{binary_string}' is: {decimal_number}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
