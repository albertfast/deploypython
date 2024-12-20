# Given a integer x, return a list of each prime number between 1 and n.
# A prime number is a number that is only divisible by itself and 1.
# (Example: 6 is not a prime number because 6 / 2 == 3. Meanwhile, 3 is a prime number because it's only divisible by itself and 1).
#
# Some code has been done for you: the function you'll actually be writing is the prime number number checker:
# Given an integer n, return True or False on whether it's a prime number or not.
# You don't have to worry about the list code if you're not familiar with lists yet.
# Note: 1 is not a prime number.

# Test #	                    Input	                    Output
# 	1                            list_of_primes(5)           [2, 3, 5]
#                                                           Each of these are the prime numbers between 1 and 5
#
#   2                           list_of_primes(10)           [2, ,3, 5, 7]
#

def list_of_primes(x):
    #Generates a list of primes numbers between 1 and x
    primes = []
    for i in range(1, x + 1):
        if is_prime(i):
            primes.append(i)
    return primes

# Complete this function to solve the problem.
def is_prime(n):
 #Returns True if n is a prime number, otherwise False
    if n <= 1:  # Numbers <= 1 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisors up to √n
        if n % i == 0:  # If n is divisible by i, it's not prime
            return False
    return True  # If no divisors are found, n is prime

# Example usage
print(list_of_primes(5))   # Output: [2, 3, 5]
print(list_of_primes(10))  # Output: [2, 3, 5, 7]