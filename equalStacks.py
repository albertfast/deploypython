#!/bin/python3
#You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. 
# You can change the height of a stack by removing and discarding its topmost cylinder any number of times.
# Find the maximum possible height of the stacks such that all of the stacks are exactly the same height.
# This means you must remove zero or more cylinders from the top of zero or more of the three stacks until
# they are all the same height, then return the height.

# Problem Açıklaması:
#
# Üç silindir yığını veriliyor. Her silindirin çapı aynı, ancak yükseklikleri farklı olabilir.
# Yığınların yüksekliğini, tepelerinden silindirleri çıkararak değiştirebilirsin.
# Amaç, üç yığını da aynı yüksekliğe getirebilmek için ulaşabileceğin en yüksek yüksekliği bulmak.
# Bu, yığınların tepesinden sıfır veya daha fazla silindir çıkararak üç yığını da aynı yüksekliğe getirmek ve bu yüksekliği döndürmek demektir.
import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    """
    Üç silindir yığınının yüksekliğini eşitlemek için en yüksek olası yüksekliği bulan fonksiyon.

    Args:
        h1: Birinci yığının silindir yükseklikleri listesi (list of integers).
        h2: İkinci yığının silindir yükseklikleri listesi (list of integers).
        h3: Üçüncü yığının silindir yükseklikleri listesi (list of integers).

    Returns:
        Eşitlenen yığınların yüksekliği (int).
    """
    
       # Örnek:
    # h1 = [1, 2, 3, 4, 5]
    # h2 = [1, 2, 3]
    # h3 = [1, 2]
    # Beklenen Sonuç: 6

    # Yığınların mevcut yüksekliklerini hesapla
    
    s1 = sum(h1)
    s2 = sum(h2)
    s3 = sum(h3)

    while True:
        if s1 == s2 == s3:
           return s1
        
        if s1 >= s2 and s1 >= s3:
            if not h1:
               return 0
            s1 -= h1.pop(0)
        elif s2 >= s1 and s2 >= s3:
             if not h2:
               return 0
             s2 -= h2.pop(0)
        else:
            if not h3:
               return 0
            s3 -= h3.pop(0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
