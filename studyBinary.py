def convert_binary_to_decimal(binary_number):
    """
    Convert a binary number to its corresponding decimal number and print the detailed computation steps.

    Args:
    binary_number (str): The binary number as a string.

    Returns:
    int: The decimal representation of the binary number.
    """
    if not all(char in '01' for char in binary_number):
        raise ValueError("Input must be a binary number containing only 0s and 1s.")

    decimal_number = 0
    detailed_steps = []
    detailed_steps_math = []
    binary_number = binary_number[::-1]  # Reverse the binary string to process from right to left

    for index, bit in enumerate(binary_number):
        power_of_two = 2 ** index
        contribution = int(bit) * power_of_two
        detailed_steps.append(f"2^{index} * {bit} = {contribution}")
        detailed_steps_math.append(f"{contribution}")
        decimal_number += contribution

    detailed_steps_math_str = " + ".join(detailed_steps_math)
    detailed_steps.append(f"\nThe final decimal number is {decimal_number}")
    print(f"The computation steps for binary {binary_number[::-1]} are:\n" + "\n".join(detailed_steps))
    print(f"\nDetailed computation: {detailed_steps_math_str} = {decimal_number}")

    return decimal_number


def convert_decimal_to_binary(decimal_number):
    """
    Convert a decimal number to its corresponding binary number and print the detailed computation steps.

    Args:
    decimal_number (int): The decimal number.

    Returns:
    str: The binary representation of the decimal number.
    """
    if decimal_number < 0:
        raise ValueError("Input must be a non-negative integer.")

    binary_number = []
    detailed_steps = []

    current_number = decimal_number
    index = 0
    while current_number > 0:
        remainder = current_number % 2
        division_result = current_number // 2
        binary_number.append(str(remainder))
        detailed_steps.append(f"{current_number} / 2 = {division_result} R{remainder} (2^{index} * {remainder})")
        current_number = division_result
        index += 1

    binary_number.reverse()
    binary_representation = "".join(binary_number)

    detailed_steps_str = "\n".join(detailed_steps)
    print(f"The binary representation for decimal {decimal_number} is {binary_representation}")
    print(f"Computation steps:\n{detailed_steps_str}")

    return binary_representation


def main():
    while True:
        print("Choose an option:")
        print("1: Convert binary to decimal")
        print("2: Convert decimal to binary")
        print("3: Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            binary_number = input("Enter a binary number: ").strip()
            try:
                decimal_number = convert_binary_to_decimal(binary_number)
                print(f"The decimal representation of the binary number '{binary_number}' is: {decimal_number}")
            except ValueError as e:
                print(e)

        elif choice == '2':
            decimal_number = input("Enter a decimal number: ").strip()
            try:
                decimal_number = int(decimal_number)
                binary_number = convert_decimal_to_binary(decimal_number)
                print(f"The binary representation of the decimal number '{decimal_number}' is: {binary_number}")
            except ValueError as e:
                print(e)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# val1 = 3
#
# new_val = 3 >> 1
#
# print(new_val) # 1


# def convert_binary_to_decimal(binary_number):
#     """
#     Convert a binary number to its corresponding decimal number and print the detailed computation steps.
#
#     Args:
#     binary_number (str): The binary number as a string.
#
#     Returns:
#     int: The decimal representation of the binary number.
#     """
#     if not all(char in '01' for char in binary_number):
#         raise ValueError("Input must be a binary number containing only 0s and 1s.")
#
#     decimal_number = 0
#     detailed_steps = []
#     binary_number = binary_number[::-1]  # Reverse the binary string to process from right to left
#
#     for index, bit in enumerate(binary_number):
#         power_of_two = 2 ** index
#         contribution = int(bit) * power_of_two
#         detailed_steps.append(f"2^{index} * {bit} = {contribution}")
#         decimal_number += contribution
#
#     detailed_steps.append(f"\nThe final decimal number is {decimal_number}")
#     detailed_explanation = " + ".join([f"2^{i} * {bit}" for i, bit in enumerate(binary_number)])
#     print(f"The computation steps for binary {binary_number[::-1]} are:\n" + "\n".join(detailed_steps))
#     print(f"\nDetailed computation: {detailed_explanation}")
#
#     return decimal_number
#
#
# def convert_decimal_to_binary(decimal_number):
#     """
#     Convert a decimal number to its corresponding binary number and print the detailed computation steps.
#
#     Args:
#     decimal_number (int): The decimal number.
#
#     Returns:
#     str: The binary representation of the decimal number.
#     """
#     if decimal_number < 0:
#         raise ValueError("Input must be a non-negative integer.")
#
#     binary_number = bin(decimal_number)[2:]  # Convert to binary and remove the '0b' prefix
#     detailed_steps = []
#     power = len(binary_number) - 1
#
#     for bit in binary_number:
#         detailed_steps.append(f"2^{power} * {bit}")
#         power -= 1
#
#     detailed_steps_str = " + ".join(detailed_steps)
#     print(f"The binary representation for decimal {decimal_number} is {binary_number}")
#     print(f"Computation steps:\n{detailed_steps_str}")
#
#     return binary_number
#
#
# def main():
#     while True:
#         print("Choose an option:")
#         print("1: Convert binary to decimal")
#         print("2: Convert decimal to binary")
#         print("3: Exit")
#
#         choice = input("Enter your choice (1/2/3): ").strip()
#
#         if choice == '1':
#             binary_number = input("Enter a binary number: ").strip()
#             try:
#                 decimal_number = convert_binary_to_decimal(binary_number)
#                 print(f"The decimal representation of the binary number '{binary_number}' is: {decimal_number}")
#             except ValueError as e:
#                 print(e)
#
#         elif choice == '2':
#             decimal_number = input("Enter a decimal number: ").strip()
#             try:
#                 decimal_number = int(decimal_number)
#                 binary_number = convert_decimal_to_binary(decimal_number)
#                 print(f"The binary representation of the decimal number '{decimal_number}' is: {binary_number}\n")
#             except ValueError as e:
#                 print(e)
#
#         elif choice == '3':
#             print("Exiting the program.")
#             break
#
#         else:
#             print("Invalid choice. Please try again.")
#
#
# if __name__ == "__main__":
#     main()
