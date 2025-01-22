# =====================Umpire===================
# Understand:
# Given an integer n, return the number of prime numbers that are strictly less than n.
# Constraints:
# 0 <= n <= 5 * 106
# Input: Take an integer greater than or equal 2
# Output: Count it until n how many prime numbers have, and print it.
# Input:    Output:
#  10        4 (2,3,5,7)
#   0        0
#   1        0
#   2        0
#   3        1
#   4        2
#   20       8

# Match:
# 1. What mental models do you think are relevant here?
#    - Prime number definition: A prime number is divisible only by 1 and itself.
#    - The Sieve of Eratosthenes algorithm for efficient prime counting.

# 2. Have you seen the same problem before?
#    - No

# 3. Have you seen a similar problem before?
#    - Yes, FizzBuzz is similar problem.

# 4. Have you seen a solution before that could be applied here with some modifications?
#    - Yes, the Sieve of Eratosthenes is a well-known algorithm that can be adapted.

# 5. Should you build a separate output list or modify the input?
#    - No input modifications are needed. Use an auxiliary list to track prime numbers.

# 6. Do you need a conditional? (if)
#    - Yes, to check if a number is prime and to mark its multiples as non-prime.

# 7. Do you need a loop? (for or while)
#    - Yes:
#      - A loop is necessary for iterating through numbers and marking multiples.

#    - Do you need a forward loop?
#      - Yes, to iterate through the numbers sequentially.

#    - Do you need a backward loop?
#      - No, backward loops are not required for this problem.

#    - Would you need to loop through the entire list or partial list?
#      - Partial loop: Only numbers up to the square root of n are checked.

# 8. Do you need nested loops?
#    - Yes:
#      - Outer loop: Iterate over numbers to determine primality.
#      - Inner loop: Mark all multiples of a prime as non-prime.

# Pseudocode:
# 1. If n is less than 2, return 0 because there are no prime numbers.
# 2. Create a list isPrime of size n and initialize all values to True.
#    - Mark isPrime[0] and isPrime[1] as False since 0 and 1 are not prime.
# 3. Use the Sieve of Eratosthenes algorithm:
#    - Start with index = 2 (the first prime number).
#    - While index * index < n:
#      a. If isPrime[index] is True:
#         - Mark all multiples of index starting from index^2 as False.
#      b. Increment index by 1.
# 4. Count the total number of True values in isPrime (this represents the count of primes).
# 5. Return the count.

# Implementation:
import numpy as np
import matplotlib.pyplot as plt
import time

# Function to test execution time of countPrimes
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # If n is less than 2, there are no prime numbers
        if n < 2:
            return 0

        # Create a list to mark numbers as prime (True) or not prime (False)
        # Initially, assume all numbers are prime
        isPrime = [True] * n

        # Mark 0 and 1 as not prime because they are not considered prime numbers
        isPrime[0] = isPrime[1] = False

        # Start checking for prime numbers from the first prime number, which is 2
        index = 2

        # Use a while loop to iterate through numbers starting from 2.
        # The loop will stop when the current number's square (index * index)
        # becomes greater than or equal to n. This is because for any non-prime number k,
        # at least one of its factors must be less than or equal to √k (square root of k).
        # Therefore, we do not need to check factors greater than k ** 0.5 .
        while index * index < n:
            # Check if the current number is still marked as prime.
            # If it is prime, we will mark all its multiples as not prime.
            if isPrime[index]:
                # Use a for loop to mark all multiples of the current prime as not prime.
                # Start from index * index to avoid redundant operations for smaller multiples.
                for multiple in range(index * index, n, index):
                    isPrime[multiple] = False
            # Move to the next number to check.
            index += 1

        # Explanation of Time Complexity:
        # The algorithm achieves an average time complexity of O(n log log n), which is highly efficient for large inputs. Here's why:
        # 1. For each prime number p, the algorithm marks its multiples as not prime.
        #    This marking process takes approximately n/p operations, where n is the input size.
        # 2. When summed over all prime numbers, this marking process results in a total cost
        #    proportional to n * (1/2 + 1/3 + 1/5 + ...), which is a harmonic series over primes.
        # 3. This harmonic series for primes mathematically converges to log log n, leading to the time complexity being O(n log log n).
        # 4. For smaller input sizes (e.g., n < 300), the actual execution time may appear faster than O(n log log n),
        #    sometimes even below O(n), due to constant factors and optimizations in memory/cache.
        # 5. However, for larger input sizes (e.g., n > 5000), the algorithm's time complexity becomes evident as O(n log log n),
        #    outperforming naive methods like O(n^2) (e.g., checking divisors individually for each number).

        # Return the count of prime numbers by summing up the True values in the list
        return sum(isPrime)


# Generate test input sizes
input_sizes = range(1, 5001, 100)  # Input sizes from 1 to 5000 incremented by 100
execution_times = []


# Test and plot
if __name__ == "__main__":
    # Test cases
    solution = Solution()
    print("Counted Prime Numbers: " ,solution.countPrimes(10))  # Expected output: 4
    print("Counted Prime Numbers: " ,solution.countPrimes(20))  # Expected output: 8
    print("Counted Prime Numbers: " ,solution.countPrimes(500))   # Expected output: 95
    print("Counted Prime Numbers: " ,solution.countPrimes(4000))   # Expected output: 550
    print("Counted Prime Numbers: " ,solution.countPrimes(5000))   # Expected output: 669


# Review & Evaluation:
# =====================
# This implementation of the Sieve of Eratosthenes efficiently counts prime numbers less than n.
# Key observations from the review:
# 1. The boolean list is_prime is correctly initialized, marking 0 and 1 as non-prime.
# 2. The algorithm iterates through numbers up to the square root of n, reducing redundant computations.
# 3. Nested loops correctly mark multiples of each prime as non-prime, starting from i^2.
# 4. The final sum of the is_prime list provides the accurate count of prime numbers less than n.
# 5. Tested cases, such as n=10 and n=20, yielded correct results with the expected prime counts.
# 6. Edge cases like n < 2 are correctly handled, returning 0 as there are no primes in this range.
# 
# Strengths:
# - Efficient use of the Sieve of Eratosthenes with O(n log(log n)) complexity.
# - Accurate and consistent handling of edge cases.

# Test cases
# print(countPrimes(10))  # Output: 4 (2, 3, 5, 7)
# print(countPrimes(0))   # Output: 0
# print(countPrimes(1))   # Output: 0
# print(countPrimes(2))   # Output: 0
# print(countPrimes(100)) # Output: 25

'''
def countPrimes(n):
    # Edge case: if n is less than 2, there are no primes
    if n < 2:
        return 0

    # Step 1: Create a boolean list to track prime numbers
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Step 2: Apply the Sieve of Eratosthenes
    for i in range(2, int(n ** 0.5) + 1):  # Only go up to the square root of n
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i * i, n, i):  # Start from i^2 to avoid redundant work
                is_prime[j] = False

    # Step 3: Count and return the number of primes
    return sum(is_prime)
'''
'''
def countPrimes(n):
    if n < 2:
        return 0

    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False

    index = 2
    while index * index < n:
        if isPrime[index]:
            for multiple in range(index * index, n, index):
                isPrime[multiple] = False
        index += 1

    return sum(isPrime)


print(countPrimes(10))
print(countPrimes(20))

'''


