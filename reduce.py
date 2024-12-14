from functools import reduce

# Define a binary function for multiplication
def multiply(x, y):
    return x * y
def plus(x,y):
    return x+ y

# Use reduce to apply the function across the list
result = reduce(multiply, [1, 2, 3, 4])

print(result)  # Output: 24 (since 1 * 2 * 3 * 4 = 24)

# Use reduce to apply the function across the list
result = reduce(plus, [1, 2, 3, 4])

print(result)  # Output: 24 (since 1 + 2 + 3 + 4 =10)

# Çarpma işlemi için
numbers = [1, 2, 3, 4]
product_result = 1  # Çarpma işlemi için başlangıç değeri 1 (çarpma işleminde etkisiz eleman)

for num in numbers:
    product_result *= num

print("Çarpım Sonucu:", product_result)  # Beklenen Çıktı: 24 (1 * 2 * 3 * 4 = 24)

# Toplama işlemi için
sum_result = 0  # Toplama işlemi için başlangıç değeri 0 (toplama işleminde etkisiz eleman)

for num in numbers:
    sum_result += num

print("Toplam Sonucu:", sum_result)  # Beklenen Çıktı: 10 (1 + 2 + 3 + 4 = 10)
