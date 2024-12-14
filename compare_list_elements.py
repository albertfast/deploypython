# Given three integers, in which two are equal to each other and the third one is different.
# Print the order number of this different one - 1, 2 or 3.

# ===================== UMPIRE ====================
# Understand:
# Problem Statement:
# - We are given three integers where two of them are equal, and one is different.
# - We need to print the order number of the different integer (1, 2, or 3).

# Input:
# - Three integers (number1, number2, number3).

# Output:
# - The position of the different integer (1 if the first number is different, 2 if the second is different, 3 if the third is different).
# - If all numbers are either the same or all different, we will print a message indicating that condition.

# Restrictions:
# - Two of the numbers must be equal, and one must be different.

# Match:
# - We will use conditional checks (if-elif-else) to identify which number is different based on equality checks.

# Plan:
# 1. Take user input for three integers.
# 2. Use conditional statements to check:
#    - If the first two numbers are equal and the third is different, print 3.
#    - If the first and third numbers are equal and the second is different, print 2.
#    - If the second and third numbers are equal and the first is different, print 1.
# 3. If all numbers are either the same or all different, print a specific message.

# Implementation:
number1 = int(input())
number2 = int(input())
number3 = int(input())

# Check which number is different by comparing each pair
if number1 == number2 and number1 != number3:
    # If the first two numbers are the same and the third is different
    print(3)  # The third number is different
elif number1 == number3 and number1 != number2:
    # If the first and third numbers are the same and the second is different
    print(2)  # The second number is different
elif number2 == number3 and number2 != number1:
    # If the second and third numbers are the same and the first is different
    print(1)  # The first number is different
else:
    # If all numbers are either the same or all different
    print("All numbers are either the same or all different.")

'''
numbers_list = [number1, number2, number3]

# Listedeki benzersiz elemanları bulmak için set kullan
unique_numbers = list(set(numbers_list))

# Eğer benzersiz elemanlardan sadece biri farklıysa
if len(unique_numbers) == 2:
    # Farklı olan sayıyı bul
    if numbers_list.count(unique_numbers[0]) == 1:
        # unique_numbers[0] farklı olan sayıdır
        different_number = unique_numbers[0]
    else:
        # unique_numbers[1] farklı olan sayıdır
        different_number = unique_numbers[1]

    # Farklı olan sayının pozisyonunu bul ve yazdır
    position = numbers_list.index(different_number) + 1
    print(position)
else:
    print("All numbers are the same or no unique number.")
'''