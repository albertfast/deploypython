#!/bin/python3
# Jesse loves cookies and wants the sweetness of some cookies to be greater than a threshold value k.
# To achieve this, Jesse combines two cookies with the least sweetness at each step.
# The sweetness of the new cookie is calculated as:
#     new_cookie_sweetness = (1 × Least sweet cookie) + (2 × 2nd least sweet cookie)

# This process is repeated until all cookies have a sweetness >= k.
# If it is not possible to reach this sweetness threshold, the function should return -1.

# The task is to determine:
# - The minimum number of operations required to make all cookies meet or exceed the sweetness threshold k.
# - If it is impossible, return -1.

# Example Input and Explanation:
# Input:
# k = 9
# A = [2, 7, 3, 6, 4, 6]

# Step-by-Step Process:
# 1. The smallest cookies are 2 and 3. Combine them:
#    new_cookie = 2 + 2 * 3 = 8
#    New array: [8, 7, 6, 6, 4]
# 2. The smallest cookies are 4 and 6. Combine them:
#    new_cookie = 4 + 2 * 6 = 16
#    New array: [16, 8, 7, 6]
# 3. The smallest cookies are 6 and 7. Combine them:
#    new_cookie = 6 + 2 * 7 = 20
#    New array: [20, 16, 8]
# 4. The smallest cookies are 8 and 16. Combine them:
#    new_cookie = 8 + 2 * 16 = 40
#    New array: [40, 20]
# At this point, all cookies have sweetness >= 9. The process stops after 4 operations.

# Example Output:
# Output: 4
# Explanation: It took 4 operations to make all cookies meet or exceed the threshold sweetness of 9.

# Function Description:
# The cookies function should take the following parameters:
# 1. INTEGER k: the threshold value
# 2. INTEGER_ARRAY A: an array of sweetness values of the cookies
# It should return:
# - INTEGER: The number of operations required, or -1 if it is not possible.

# Constraints:
# - 1 <= n <= 10^6, where n is the size of the array A
# - 0 <= k <= 10^9
# - 0 <= A[i] <= 10^6, where A[i] is the sweetness of the i-th cookie

# Example Input 1:
# k = 9
# A = [2, 7, 3, 6, 4, 6]
# Example Output 1:
# 4

# Example Input 2:
# k = 7
# A = [1, 2, 3, 9, 10, 12]
# Example Output 2:
# 2

# Approach:
# - Use a Min-Heap (priority queue) to always access the two smallest cookies efficiently.
# - Combine the two smallest cookies until all cookies meet or exceed the threshold sweetness k.
# - If there are fewer than 2 cookies left and the threshold is not met, return -1.

import math
import os
import random
import re
import sys


# Colored output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

import heapq

def cookies(k, A):
    # Debug logging
    print(f"{Colors.OKCYAN}Initial heapify: {A}{Colors.ENDC}")
    heapq.heapify(A)
    minVal = heapq.heappop(A)
    if minVal >= k: 
        print(f"{Colors.OKGREEN}All cookies already >= k: {minVal} >= {k}{Colors.ENDC}")
        return 0
    
    heapq.heappush(A, minVal)
    count = 0
    while len(A) >= 2:
        min1 = heapq.heappop(A)
        min2 = heapq.heappop(A)
        print(f"{Colors.OKBLUE}Combining {min1} and {min2}{Colors.ENDC}")
        heapq.heappush(A, min1 + min2 * 2)
        count += 1
        minNew = heapq.heappop(A)
        print(f"{Colors.WARNING}New minimum after combining: {minNew}{Colors.ENDC}")
        if minNew >= k: 
            print(f"{Colors.OKGREEN}All cookies >= k after {count} operations.{Colors.ENDC}")
            return count
        heapq.heappush(A, minNew)
    print(f"{Colors.FAIL}Not enough sweetness, returning -1.{Colors.ENDC}")
    return -1

# Add tests
def test_cookies():
    test_cases = [
        {"k": 9, "A": [2, 7, 3, 6, 4, 6], "expected": 4},
        {"k": 10, "A": [1, 1, 1], "expected": -1},
        {"k": 7, "A": [1, 2, 3, 9, 10, 12], "expected": 2},
        {"k": 15, "A": [1, 2, 3, 9, 10, 12], "expected": 2},
        {"k": 20, "A": [10, 12], "expected": 1},
    ]

    total_passed = 0
    for i, test in enumerate(test_cases):
        print(f"{Colors.HEADER}Test Case {i + 1}:{Colors.ENDC}")
        print(f"  Input k: {test['k']}, A: {test['A']}")
        result = cookies(test["k"], test["A"])
        if result == test["expected"]:
            print(f"{Colors.OKGREEN}  Passed ✅{Colors.ENDC}")
            total_passed += 1
        else:
            print(f"{Colors.FAIL}  Failed ❌{Colors.ENDC}")
            print(f"    Expected: {test['expected']}, Got: {result}")
        print("-" * 40)

    print(f"{Colors.BOLD}Summary:{Colors.ENDC} {total_passed}/{len(test_cases)} tests passed.")

if __name__ == "__main__":
    # Uncomment for competitive programming environment
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
    """
    # Run tests for debugging
    test_cookies()