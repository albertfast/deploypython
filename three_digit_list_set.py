# Kullanıcıdan üç basamaklı bir sayı girmesini istiyoruz.
digit_three = int(input("Üç basamaklı bir sayı girin: "))

# Sayıyı metin (string) formatına çeviriyoruz.
# Bu, sayının her bir basamağını ayrı ayrı işlememizi sağlar.
digit_three_str = str(digit_three)

# Metin formatındaki sayıyı basamaklarına ayırarak bir liste oluşturuyoruz.
# Bu liste içinde her bir basamak tamsayı olarak saklanacak.
digit_three_list = [int(d) for d in digit_three_str]

# Basamakları bir küme (set) yapısına dönüştürüyoruz.
# Küme yapısı aynı değerden sadece bir tane saklar, bu yüzden benzersiz basamakları elde ederiz.
digits = set(digit_three_list)

# Basamakların benzersiz olup olmadığını kontrol ediyoruz.
# Eğer liste uzunluğu ile küme uzunluğu aynıysa, tüm basamaklar benzersizdir.
unique_digits = len(digit_three_list) == len(digits)

# Basamakların artan sırada olup olmadığını kontrol ediyoruz.
# Basamaklar sıralıysa, sorted(digit_three_list) ile eşit olur.
is_in_order = digit_three_list == sorted(digit_three_list)

# Üç şartı birden kontrol ediyoruz:
# 1. Basamaklar benzersiz mi? (unique_digits True olmalı)
# 2. Basamaklar artan sırada mı? (is_in_order True olmalı)
# 3. Girilen sayı gerçekten üç basamaklı mı?
if unique_digits and is_in_order and len(str(digit_three)) == 3:
    # Eğer tüm şartlar sağlanıyorsa "YES" yazdırıyoruz.
    print("YES")
else:
    # Şartlardan herhangi biri sağlanmazsa "NO" yazdırıyoruz.
    print("NO")
