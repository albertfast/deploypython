def dec_to_bin(n):
    """
    Convert a decimal number to a binary string with computation details.

    Args:
    n (int): An integer between 1 - 1000

    Returns:
    str: A string representing the binary representation of n
    """
    if n < 1 or n > 1000:
        raise ValueError("Input must be an integer between 1 and 1000.")

    binary_representation = []
    detailed_steps = []

    current_number = n
    while current_number > 0:
        remainder = current_number % 2
        division_result = current_number // 2
        binary_representation.append(str(remainder))
        detailed_steps.append(f"{current_number} / 2 = {division_result} R{remainder}")
        current_number = division_result

    binary_representation.reverse()
    binary_str = "".join(binary_representation)

    # Print detailed computation steps
    # print(f"Converting decimal {n} to binary:")
    # for step in detailed_steps:
    #     print(step)

    return binary_str


def main():
    try:
        n = int(input().strip()) # "Enter a decimal number between 1 and 1000: "
        binary_str = dec_to_bin(n)
        print(f"{binary_str}")
        print("My favorite number is:", 9)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
