# =====================Umpire===================
# Understand:
# Find the first digit of the factorial of a given non-negative number, n.
# Input : Take an integer input, and calculate factorial value.
# Output : Print it factorial value first digit
# Example:  Input:      Output:
#             4           2 (4! = 24)
#             6           7 (6! = 720)

# Match: Factorial
# - Mental models: Pattern Recognition and First-Principles Thinking.
# - Same problem: No
# - Similar problem: Yes, Factorial.py.


# log10(x) = ln(x) / ln(10) formula
# log10(x) = y  ==> 10^y = x
# log10(120) = 2.079181 ==> So we can say 10^2.079181 = 120
# And we can say this number is between 100 and 999 because (2.079181) == 2 + 0.079181

# log10(99) = 1.995635, cumulative log_sum = 155.970004  this number is between 10 and 99 because (1.995635) == 1 + 0.079181

# log_sum= log10(1) + log10(2) + log10(3) + ... + log10(n)

# log10(1) = 0.000000, cumulative log_sum = 0.000000
# log10(2) = 0.301030, cumulative log_sum = 0.301030
# log10(3) = 0.477121, cumulative log_sum = 0.778151
# log10(4) = 0.602060, cumulative log_sum = 1.380211
# log10(5) = 0.698970, cumulative log_sum = 2.079181

# remaining part will give us first digit
# 5! = cumulative log_sum = 2.079181 ==> this number is between 100 and 999 because (2.079181) == 2 + 0.079181
# So 10^0.079181 = 1.19 ==> 1 + 0.19  ==> 1 is our first digit :)
# Property of Logarithms:
# log10(a * b) = log10(a) + log10(b)
# This property allows us to express products, such as factorials, as a sum of logarithms.
# Fractional Part and First Significant Digit:
#
# The fractional part of a logarithm represents the significant portion of a number, independent of its scale. Using:
# n!≈10^integerpart+fractionalpart
# we can directly extract the first significant digit of the number.

# import math
# print(math.log10(5))  # 0.698970
# ln_5 = math.log(5)  # Doğal logaritma (tabanı e)
# ln_10 = math.log(10)
# print(ln_5, "and", ln_10)
# x = 1.6094379124341003 / 2.302585092994046
# print("log10(5) = ",x)

# Pseudocode for Finding the First Digit of a Factorial Using Logarithms
# 1. Define the function firstFactorialDigit(n):
#     a. If n < 2:
#         - Print a message explaining factorial is 1 for n=0 or n=1.
#         - Return 1 as the first digit.
# 
# 2. Initialize log_sum to 0.
# 
# 3. For each number i from 1 to n:
#     a. Compute the base-10 logarithm of i.
#     b. Add the logarithm to log_sum.
#     c. Print the current logarithm and updated log_sum.
# 
# 4. Extract the fractional part of log_sum:
#     a. Subtract the integer part from log_sum.
#     b. Print the fractional part.
# 
# 5. Compute the first significant digit:
#     a. Raise 10 to the power of the fractional part.
#     b. Convert the result to an integer.
#     c. Print the most significant digit.
# 
# 6. Return the most significant digit.
# 
# 7. In the main program:
#     a. Prompt the user to enter a number.
#     b. Call firstFactorialDigit with the input number.
#     c. Print the result.



import math
def firstFactorialDigit(n):
    """
    Calculate the most significant digit of n!.
    """
    if n < 2:
        print("Since n is less than 2, factorial is 1.")
        return 1  # For n=0 or n=1, factorial is 1.

    # Use logarithms to compute the significant part of the factorial.
    log_sum = 0
    print(f"Calculating the sum of log10 values for numbers from 1 to {n}:")

    for i in range(1, n + 1):
        current_log = math.log10(i)  # Logarithm base 10 of the current number
        log_sum += current_log
        print(f"log10({i}) = {current_log:.6f}, cumulative log_sum = {log_sum:.6f}")

    # Extract the most significant digit from log_sum
    fractional_part = log_sum - int(log_sum)  # Get the fractional part
    print(f"\nThe fractional part of log_sum is {fractional_part:.6f}")

    significant_digit = int(10 ** fractional_part)  # Convert fractional part to a number
    print(f"The most significant digit calculated from 10^({fractional_part:.6f}) is {significant_digit}\n")

    return significant_digit


if __name__ == "__main__":
    number = int(input("Enter a number to find the first digit of its factorial: "))
    print("The first digit of the factorial is:", firstFactorialDigit(number))
# print(math.log10(2))
# print(math.log10(5000))
# print(math.log10(100))



