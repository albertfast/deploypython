# ================================UMPIRE========================================
# Understand:
# Imagine your program only accept an integer number that is within a given
# range of values. Write your program in such a way that in an event the
# user enters an invalid entry, the program ask for the same input until
# the user gets it correct. Once the user enters a valid input, the rest
# of the program allowed to continue.
#
# Input = a number
# output = the validated number
# start = 10,
# end = 100,
# Ex. input = "code" need to ask again
# Ex. input = 110 need to ask again
# Ex. input = 9 need to ask again
# input = 30 => validated
# need to ask this is not a number or > 100 or < 10
# Match: for loop with a break
#
# Plan:
# 1. input number
# 2. while number is not an integer or the number > 100 or the number < 10:
# 2.1 input number
# 3. covert the number into an integer
# 4. allow the flow to continue
# Implement:

number = input("Enter the number: ")
while not number.isdecimal() or (int(number) > 100 or int(number) < 10):
    number = input("Invalid number. Try again. ==>  ")
print("Valid number received")
number = int(number)

# ================================UMPIRE========================================
# Understand:
# Input: Take user input integer
# Output: Reverse the integer input by the user
# Restriction : Take user input greater than 9
# Example : Input : 1234 Output: 4321

n = int(input("Enter the number (greater than 9): "))
reverse_number = 0

# Check if the number is greater than 9
if n > 9:
    while n > 0:
        remainder = n % 10  # Get the last digit
        print(f"Current last digit (remainder): {remainder}")  # Show the last digit extracted

        reverse_number = (reverse_number * 10) + remainder  # Append last digit to the reversed number
        print(f"Updated reversed number: {reverse_number}")  # Show the current state of reversed number

        n = n // 10  # Remove the last digit from n
        print(f"Remaining number after removing last digit: {n}")  # Show the remaining part of n

    print("Final Reversed number:", reverse_number)
else:
    print("Please enter a number greater than 9.")

# Kullanıcıdan sayıyı al
n = int(input("Enter the number (greater than 9): "))

# Basamakları listeye ekleyelim
digits = []
while n > 0:
    remainder = n % 10
    digits.append(remainder)
    n = n // 10

# Listeyi ters çevirerek sayıyı oluştur
reversed_number = int("".join(map(str, digits)))
print("Final Reversed number:", reversed_number)


