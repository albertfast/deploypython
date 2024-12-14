# Understand:
# Given two positive integers n and m, create a two-dimensional array of size n×m and populate it with the characters "." and "*"
# in a chequered pattern. The top left corner should have the character "." .

def create_chequered_pattern(n, m):
    # n x m boyutunda iki boyutlu bir matris oluştur
    matrix = [["." if (i + j) % 2 == 0 else "*" for j in range(m)] for i in range(n)]

    # Matrisi satır satır yazdır
    for row in matrix:
        print(" ".join(row))


# Kullanıcıdan n ve m değerlerini al ve fonksiyonu çağır
n, m = map(int, input("Enter number of rows and columns (n m): ").split())
create_chequered_pattern(n, m)
