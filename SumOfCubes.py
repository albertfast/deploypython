# ================================UMPIRE========================================
# Understand:
# For the given integer N calculate the following sum:
#
# 1³ + 2³ + ... + N³
# Example: N = 3 =>  1³ + 2³ + 3³ = 36

# Match: Sum of N numbers
number = int(input())
sum = 0
for i in range(1,number + 1):
    sum += i ** 3
print(sum)
