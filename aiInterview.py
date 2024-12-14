def get_even_numbers():
    numbers = input()
    number_list = [int(num.strip()) for num in numbers.split(",")]
    even_numbers = [num for num in number_list if num % 2 == 0]

    return even_numbers
output = get_even_numbers()
print(output)

###########################################################

def reverse_string(input_string):
    return input_string[::-1]

input_str = "hello"
output_str = reverse_string(input_str)
print(output_str)

###########################################################

def first_non_repeating_character(s):
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in s:
        if char_count[char] == 1:
            return char
    return None

input_string = "swiss"
output = first_non_repeating_character(input_string)
print(output)

