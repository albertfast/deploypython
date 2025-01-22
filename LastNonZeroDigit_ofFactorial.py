# =====================Umpire===================
# Understand:
# Find the last non-zero digit of the factorial of a given non-negative number, n.
# Input : Take an integer input, and calculate factorial value.
# Output : Print it factorial value of last non-zero digit
# Example:  Input:      Output:
#             4           4 (4! = 24)
#             6           2 (6! = 720 ==> 72 (2))

# =====================Match===================
# Mental models relevant here:
#  Modular arithmetic to handle the last digit efficiently.
#  Removing trailing zeros by repeatedly dividing by 10.

# Have you seen the same problem before?
#  Yes, the "Last Digit of Factorial" problem is similar but without focusing on zeros.

# Have you seen a similar problem before?
#  Yes, identifying patterns in digits and handling factorial calculations.

# Have you seen a solution before that could be applied here with some modifications?
#  Yes, solutions involving modulo operation to extract specific digits can be adapted.

# Should you build a separate output list or modify the input?
#  No need for an output list or input modification; the focus is on direct calculations.

# Do you need a conditional? (if)
#  Yes, to handle cases for small inputs (e.g., n = 0 or n < 5).

# Do you need a loop? (for or while)
#  Yes, a forward loop to calculate the factorial and another loop to remove trailing zeros.

# Do you need a forward loop?
#  Yes, to iterate through numbers from 1 to n for factorial calculation.

# Do you need a backward loop?
#  No, not necessary for this solution.

# Would you need to loop through the entire list or partial list?
#  Loop through all integers from 1 to n.

# Do you need nested loops?
#  No, a single loop for factorial and one for removing trailing zeros is sufficient.

# Pseudocode for Finding Last Non-Zero Digit of Factorial
# Initialize an array dig to store the last non-zero digit for numbers 0 to 9.
# Example: dig = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]

# Define a function lastNon0Digit(n):
    # Base case:
    # If n < 10, return dig[n], as the result for small numbers is precomputed.

    # For n >= 10:
    # Check the tens digit of n by computing (n//10) % 10:
        # If the tens digit is even:
            # Use the formula: (6 * lastNon0Digit(n // 5) * dig[n % 10]) % 10
        # If the tens digit is odd:
            # Use the formula: (4 * lastNon0Digit(n // 5) * dig[n % 10]) % 10

# Return the calculated value for the last non-zero digit of n!.

# Driver code:
# Input a value for n.
# Call the lastNon0Digit(n) function.
# Print the result.

# Precomputed last non-zero digits for numbers 0-9
PRECOMPUTED_DIGITS = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]

def last_non_zero_digit(n):
    """
    Efficiently calculates the last non-zero digit of n! using recursion.
    :param n: Non-negative integer
    :return: Last non-zero digit of n!
    """
    # Base case: If n is less than 10, return the precomputed value
    if n < 10:
        return PRECOMPUTED_DIGITS[n]

    # Recursive case
    # Calculate last non-zero digit based on whether tens digit is even or odd
    if ((n // 10) % 10) % 2 == 0:  # Tens digit is even
        return (6 * last_non_zero_digit(n // 5) * PRECOMPUTED_DIGITS[n % 10]) % 10
    else:  # Tens digit is odd
        return (4 * last_non_zero_digit(n // 5) * PRECOMPUTED_DIGITS[n % 10]) % 10

# Take input from the user
if __name__ == "__main__":
    try:
        n = int(input())
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            print(last_non_zero_digit(n))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


# Review & Evaluate: Last Non-Zero Digit of Factorial
# Base case: If n is less than 10, return the precomputed value
# Check if the tens digit (second last digit) of n is odd or even
# Apply the formula based on the parity of the tens digit
# 1. The code uses recursion efficiently to calculate the result without explicitly computing the factorial.
# 2. The precomputed values for digits 0 to 9 ensure that the base case is handled quickly.
# 3. Recursive calls reduce the problem size, making the algorithm efficient for larger inputs.
# 4. Proper formulas are applied based on the parity of the tens digit of n.
# 5. Each step of the recursive evaluation was verified using Python Tutor to ensure correctness.
# Time complexity: O(log n)
# Space complexity: O(log n)

"""
# Function to calculate the last non-zero digit of a factorial
def last_non_zero_digit(n):
    def helper(num, result, count_five):
        # Base case: Stop recursion when num == 1
        if num <= 1:
            return

        # Count how many times 5 divides the current number
        original_num = num
        while num % 5 == 0:
            num //= 5
            count_five += 1

        # Balance 5s with 2s by dividing num by 2
        while count_five > 0 and num % 2 == 0:
            num //= 2
            count_five -= 1

        # Update the result with the current number (mod 10)
        result[0] = (result[0] * (num % 10)) % 10

        # Recursive call for the next number (reduce by 1)
        helper(original_num - 1, result, count_five)

    # Initialize variables
    result = [1]
    helper(n, result, 0)
    return result[0]

# Take input from the user
if __name__ == "__main__":
    try:
        n = int(input())
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            print({last_non_zero_digit(n)})
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
# Okunabilirlik ve Basitlik Açısından: İkinci kod, mantığını anlamak açısından daha basit olabilir çünkü açıkça 5'leri ve 2'leri dengelemeye odaklanıyor.
"""








