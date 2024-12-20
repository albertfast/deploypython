#Given a string of four numbers, print "Even" if the summation of all of the numbers is even, and "Odd" if the summation is odd.

#numbers = []
#for i in range(4):
    #number = int(input())
    #numbers.append(number)
numbers = list(map(int, input().split())) #"Enter four numbers separated by spaces: "
total = sum(numbers)

if total % 2 == 0:
    print("Even")
else:
    print("Odd")

# Kullanıcıdan bir dizi girdi al
numbers = list(map(int, input("Enter four numbers separated by spaces: ").split()))

# Sayıların toplamını hesapla
total = sum(numbers)

# Sayıların artan sırada olup olmadığını kontrol et
is_sorted = numbers == sorted(numbers)

# Durumları kontrol edip uygun çıktıyı yazdır
if is_sorted:
    if total % 2 == 0:
        print("Sorted & even")
    else:
        print("Sorted & odd")
else:
    if total % 2 == 0:
        print("Unsorted & even")
    else:
        print("Unsorted & odd")



