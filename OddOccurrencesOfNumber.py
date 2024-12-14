# Understand:
# Given an array/list nums containing n unsorted numbers between -3 * 104 and 3 * 104
# return the only number that appears odd number of times in the array/list.
# Constraints: Build a solution with O(n) time complexity and uses constant space (O(1) Space Complexity.
# Note: The range is -3 * 10^4 and 3 * 10^4
#
# Example:                                           input:                     output:
#                                               [3, 1, 1]                       return 3
#                                               [-2, 4, 1, 4, -2, 4, 1]         returns 4
# Plan:
# XOR eliminates duplicate elements. For any number a, a ^ a = 0. Hence, when a number appears an even number of times, it effectively cancels itself out.
# XOR with 0 returns the number itself: a ^ 0 = a. This ensures that single elements (odd occurrences) are preserved.
# XOR is commutative and associative, meaning the order of operations doesn't matter, allowing us to traverse the list in one pass.
# Note: This XOR method works only if there is exactly one number that appears an odd number of times in the list.
# If more than one number appears an odd number of times, this method will not work.


# XOR, aynı elemanları birbirinden sıfırlar. Örneğin, herhangi bir sayı için a ^ a = 0. Bu nedenle, bir sayı çift sayıda geçtiğinde kendini iptal eder.
# XOR işlemi, bir sayı 0 ile XOR'landığında sonucu aynen döner: a ^ 0 = a. Bu, tekil (tek sayıda geçen) elemanların korunmasını sağlar.
# XOR, birleştirilebilir (associative) ve değişmeli (commutative) bir işlemdir. Bu da listeyi herhangi bir sırada tek geçişte işlememize olanak tanır.
# Not: Bu XOR yöntemi, yalnızca dizide tam olarak bir adet tekil (tek sayıda geçen) eleman varsa çalışır.
# Eğer birden fazla eleman tek sayıda geçiyorsa, bu yöntem doğru sonucu vermez.


# Implementation:

import math
from collections import Counter

def odd_occurrences_of_number(nums):
    result = 0  # Başlangıç değeri
    print(f"Başlangıç: result = {result} (binary: {bin(result)})")

    for i, num in enumerate(nums):
        if num < math.pow(10, 4) * -3 or num > math.pow(10, 4) * 3:
            raise ValueError("Numbers have to be between -3 * 10^4 and 3 * 10^4 ")
        print(f"\nIndex {i}, Eleman: {num} (binary: {bin(num)})")
        print(f"Önceki result: {result} (binary: {bin(result)})")

        # XOR işlemi
        result ^= num
        print(f"Yeni result (XOR sonrası): {result} (binary: {bin(result)})")

        # XOR işleminin bit seviyesinde detaylı açıklaması
        xor_binary = bin(result ^ num)[2:].zfill(16)  # XOR yapılmadan önceki ikili gösterimi
        print(
            f"Bit düzeyinde XOR: {bin(result)[2:].zfill(16)} ^ {bin(num)[2:].zfill(16)} = {bin(result)[2:].zfill(16)}")

    print(f"\nSonuç: {result} (Tek sayıda geçen sayı)")
    return result

# nums = [3, 1, 1]
# print(odd_occurrences_of_number(nums))
#
# nums = [-2, 4, 1, 4, -2, 4, 1]
# print(odd_occurrences_of_number(nums))

nums = [3000, -15,-15,-11,2,-249, 2,-15,7,11,-15, -11, 3000, -249, 7]
print(odd_occurrences_of_number(nums))

nums = [1, 2, 3, 2, 2, 1, 4, 4, 1]
count = Counter(nums)

even_occurrences = [num for num, freq in count.items() if freq % 2 == 0]
print(even_occurrences)