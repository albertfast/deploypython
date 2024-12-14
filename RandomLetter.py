import random

def random_letter(ex_str, seed):
    random.seed(seed)  # Set the seed for reproducible results
    return random.choice(ex_str)  # Select a random character from the string

# Taking input from the user for the string and seed
input_string = input("Enter a string: ")
input_seed = int(input("Enter a seed value (integer): "))

# Calling the function and printing the result
result = random_letter(input_string, input_seed)
print(f"Random character from '{input_string}' with seed {input_seed}: {result}")
