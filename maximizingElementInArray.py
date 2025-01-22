#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxElement' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER maxSum
#  3. INTEGER k
#

def maxElement(n, maxSum, k):
    def calculateSum(peak, n, k):
        left_count = min(peak - 1, k)
        right_count = min(peak - 1, n - k - 1)

        left_sum = (peak - 1 + peak - left_count) * left_count // 2
        right_sum = (peak - 1 + peak - right_count) * right_count // 2

        sum_val = peak + left_sum + right_sum + (k - left_count) + (n - k - 1 - right_count)

        return sum_val

    left, right, result = 1, maxSum, 0
    while left <= right:
        mid = (left + right) // 2
        if calculateSum(mid, n, k) <= maxSum:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    maxSum = int(input().strip())

    k = int(input().strip())

    result = maxElement(n, maxSum, k)

    fptr.write(str(result) + '\n')

    fptr.close()
