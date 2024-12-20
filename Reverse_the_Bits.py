def bin_to_dec(s):
    if not s.strip():
        raise ValueError("Input cannot be empty.")

    if not all(char in '01' for char in s):
        raise ValueError("Input must be a binary number containing only 0s and 1s.")

    if len(s) > 10 or len(s) < 1:
        raise ValueError("Input must be a binary string between 1 and 10 characters long.")

    decimal_number = 0
    length = len(s)

    for index, bit in enumerate(s):
        power_of_two = length - 1 - index
        contribution = int(bit) * (2 ** power_of_two)
        decimal_number += contribution

    return decimal_number


def main():
    number = int(input())

    if number <= 9:
        print("Error: Number must be greater than 9.")
        return

    number_bin = bin(number)[2:]  # binary representation without '0b' prefix
    #last_two_bits = number_bin[-2:]  # last two bits
    reversed_bits = number_bin[::-1]  # reverse the bits

    try:
        decimal_number = bin_to_dec(reversed_bits)
        print(f"{decimal_number}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
