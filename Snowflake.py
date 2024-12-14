# Understand:
# Given an odd positive integer n, produce a two-dimensional array of size n×n.
# Fill each element with the character "." . Then fill the middle row, the middle column and the diagonals with the character "*".
# You'll get an image of a snowflake. Print the snowflake in n×n rows and columns and separate the characters with a single space.
# Example:         Input:       Output:
#                               *..*..*
#                               .*.*.*.
#                               ..* * *..
#                       7       * * * * * * *
#                               ..* * *..
#                               .*.*.*.
#                               *..*..*


# Kullanıcıdan bir tam sayı alınıyor (n: matrisin boyutu)
n = int(input("Enter an odd positive integer: "))
# Kar tanesi desenini oluşturan fonksiyon
def create_snowflake(n):
    # n x n boyutunda bir matris oluşturuluyor, tüm elemanları başlangıçta "."
    matrix = [["." for _ in range(n)] for _ in range(n)]

    # Ortadaki satır ve sütunun indeksi hesaplanıyor
    middle = n // 2

    # Matrisin elemanlarını doldur
    for i in range(n):
        matrix[i][i] = "*"  # Ana köşegen (soldan sağa)
        matrix[i][n - i - 1] = "*"  # Yan köşegen (sağdan sola)
        matrix[middle][i] = "*"  # Ortadaki satır
        matrix[i][middle] = "*"  # Ortadaki sütun

    # Matris satır satır yazdırılıyor
    for row in matrix:
        print(" ".join(row))

    # n değeri döndürülüyor (opsiyonel, aslında gerek yok)
    return n


# Fonksiyon çağrılıyor
create_snowflake(n)
