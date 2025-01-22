# =====================Umpire===================
# Understand:
# Find the last digit of the factorial of a given non-negative number, n.
# Take an integer input, then find a factorial value
# Print it output which is factorial value last digit
# Example:  Input:      Output:
#             4           4 (4! = 24)
#             6           0 (6! = 720)

# Match Questions:
# 1. What mental models do you think are relevant here?
#    - "Pattern Recognition" and "First-Principles Thinking."
#    - Identify and interpret recurring patterns in the problem.
#    - Analyze the root cause of the behavior using logical reasoning.

# 2. Have you seen the same problem before?
#    - Yes, a similar problem was solved in Course 201 while working on Factorial.py and Sum of Factorials problems.

# 3. Have you seen a similar problem before?
#    - Yes, calculating factorial values and analyzing their patterns.

# 4. Have you seen a solution before that could be applied here with some modifications?
#    - Yes, the solution for calculating factorials can be reused here with an additional step to extract the last digit.

# 5. Should you build a separate output list or modify the input?
#    - No need to modify the input or build a separate list.

# 6. Do you need a conditional? (if)
#    - Yes, for handling the base case when n = 0.

# 7. Do you need a loop? (for or while)
#    - Yes, a forward loop (for) to calculate the factorial iteratively.

# 8. Do you need a forward loop?
#    - Yes, to iterate from 1 to n.

# 9. Do you need a backward loop?
#    - No, a backward loop is not necessary.

# 10. Would you need to loop through the entire list or partial list?
#     - No lists are used, just numbers.

# 11. Do you need nested loops?
#     - No, nested loops are not required for this solution.


# Pseudocode:
#     1. Input: A non-negative integer n.
#     2. Output: The last digit of the factorial of n.
#
#     Steps:
#     1. Handle the base case:
#         - If n is 0, return 1 (since 0! = 1).
#     2. Precompute the last digit for smaller values of n:
#         - If n is 1 or 2, return n (1! = 1, 2! = 2).
#         - If n is 3, return 6 (3! = 6).
#         - If n is 4, return 4 (4! = 24, last digit = 4).
#     3. Handle large inputs:
#         - For n > 4, return 0 directly because factorials of numbers greater than 4
#           include both 2 and 5, resulting in a product divisible by 10, which always
#           has a last digit of 0.


def last_digit_factorial(n):
    """
    Calculates the last digit of the factorial of a given non-negative integer n.
    This optimized approach returns precomputed values for n <= 4 and directly
    returns 0 for n > 4, as factorials of numbers greater than 4 always have
    a last digit of 0.

    :param n: Non-negative integer
    :return: Last digit of n!
    """
    # Base cases
    # If n is 0, return 1 (since 0! = 1).
    if n == 0:
        return 1  # 0! = 1
    # If n is 1 or 2, return n (1! = 1, 2! = 2).
    elif n <= 2:
        return n  # 1! = 1, 2! = 2
    # If n is 3, return 6 (3! = 6).
    elif n == 3:
        return 6  # 3! = 6
    # If n is 4, return 4 (4! = 24, last digit = 4).
    elif n == 4:
        return 4  # 4! = 24, last digit = 4

    # For n > 4, factorial includes both 2 and 5, so last digit is 0
    else:
        return 0

if __name__== "__main__":
    print("Last digit 15! is = ",last_digit_factorial(15))
    print("Last digit 4! is =  ", last_digit_factorial(4))
    print("Last digit 6! is =  ", last_digit_factorial(6))
    print("Last digit 3! is =  ", last_digit_factorial(3))
    print("Last digit 1! is =  ", last_digit_factorial(1))
    print("Last digit 2!is  =  ", last_digit_factorial(2))
# Example usage
#print(last_digit_factorial(15))  # Output: 0

# ====================== Review & Evaluate ======================
# Thinking Model:
# - Observed through pattern recognition that factorials of n > 4 always end with 0.
# - Used logical deduction to optimize the solution by precomputing values for n <= 4.
# - Efficiently handles larger inputs with constant-time return for n > 4.
# Time Complexity Analysis:
# - O(1): The solution directly returns results for all inputs without loops or recursion.
# - No iterations or calculations are performed, making it constant time.
# Space Complexity Analysis:
# - O(1): No additional space is used apart from a few variables.
# Pros of this Approach:
# - Very efficient for all inputs.
# - Avoids unnecessary computations for large factorials, making it ideal for constraints.
# Cons of this Approach:
# - The solution heavily relies on the observation that n > 4 always results in a last digit of 0.
# - If the problem changes (e.g., for a different modulus), this approach would need modification.
# Potential Improvements:
# - This solution is already optimal for the problem constraints.
# - For more general cases (e.g., finding the last k digits), an iterative or modular arithmetic approach may be needed.

# Driver code
# print(last_digit_factorial(0))
# print(last_digit_factorial(1))
# print(last_digit_factorial(2))
# print(last_digit_factorial(3))
# print(last_digit_factorial(4))
# print(last_digit_factorial(3))
# print(last_digit_factorial(0))
# print(last_digit_factorial(32))
# print(last_digit_factorial(2))