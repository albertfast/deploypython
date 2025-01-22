#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'stockPairs' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stocksProfit
#  2. LONG_INTEGER target
#

def stockPairs(stocksProfit, target):
    seen = set()
    pairs = set()

    for profit in stocksProfit:
        complement = target - profit
        if complement in seen:
            pair = (min(profit, complement), max(profit, complement))
            pairs.add(pair)
        seen.add(profit)

    return len(pairs)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stocksProfit_count = int(input().strip())

    stocksProfit = list(map(int, input().rstrip().split()))

    target = int(input().strip())

    result = stockPairs(stocksProfit, target)

    fptr.write(str(result) + '\n')

    fptr.close()

# Test cases
if __name__ == "__main__":
    # Test case 1
    stocksProfit = [1, 3, 46, 1, 3, 9]
    target = 47
    print("Test 1:", stockPairs(stocksProfit, target))  # Expected output: 1

    # Test case 2
    stocksProfit = [6, 6, 3, 9, 3, 5, 1]
    target = 12
    print("Test 2:", stockPairs(stocksProfit, target))  # Expected output: 2

    # Test case 3
    stocksProfit = [1, 2, 3, 4, 5, 6]
    target = 7
    print("Test 3:", stockPairs(stocksProfit, target))  # Expected output: 3

    # Test case 4
    stocksProfit = [5, 5, 5, 5, 5]
    target = 10
    print("Test 4:", stockPairs(stocksProfit, target))  # Expected output: 1

    # Test case 5
    stocksProfit = []
    target = 5
    print("Test 5:", stockPairs(stocksProfit, target))  # Expected output: 0


