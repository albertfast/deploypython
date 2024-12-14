# Kullanıcıdan boşlukla ayrılmış sayılar alıyoruz
user_input = input("Enter numbers separated by spaces: ")

# Alınan girdiyi parçalara ayırıp her bir öğeyi tam sayıya çevirip listeye ekliyoruz
numbers_list = []
for num in user_input.split():
    numbers_list.append(int(num))

# Her bir sayı üzerinde işlem yapıyoruz
for number in numbers_list:
    divisor = 2  # En küçük böleni kontrol etmeye 2’den başlıyoruz

    # En küçük böleni bulmak için while döngüsü
    while number % divisor != 0:
        divisor += 1  # Eğer bölen değilse, bir sonraki sayıya geç

    # Sonuç olarak, en küçük böleni yazdırıyoruz
    print(f"{number}:{divisor}", end= " " )
