def faktoryel(n):
    """
    Bir sayının faktöriyelini hesaplar.

    Adımlar:
    1. `result` değişkeni 1 olarak başlatılır.
    2. 1'den n'e kadar tüm sayılarla çarpım yapılır.
    3. Hesaplanan değer döndürülür.

    Big-O Analizi:
    - Zaman Karmaşıklığı (Time Complexity): O(n)
    - Alan Karmaşıklığı (Space Complexity): O(1)
    """

    # Faktöriyel sonucunu saklamak için başlangıç değeri
    result = 1  # Başlangıç: 1

    # 1'den n'e kadar döngü ile çarpımlar
    for i in range(1, n + 1):
        result = result * i  # Her i değeri ile çarp
        print(f"Adım {i}: result = {result}")  # Ara sonuçları göster

    # Hesaplanan faktöriyel sonucunu döndür
    return result


# Test Çalıştırmaları
print("3! için faktöriyel:")
print(f"Sonuç: {faktoryel(3)}")  # Beklenen Çıktı: 6

print("\n8! için faktöriyel:")
print(f"Sonuç: {faktoryel(8)}")  # Beklenen Çıktı: 40320

print("\n12! için faktöriyel:")
print(f"Sonuç: {faktoryel(12)}")  # Beklenen Çıktı: 479001600

# Faktöriyel değerlerini saklamak için bir liste (O(n) alan karmaşıklığı - n = 13)
factorial_list = [0] * 13


# Faktöriyel hesaplama ve listeyi doldurma fonksiyonu
def calculatefact():
    # Başlangıç değeri
    result = 1  # O(1) sabit zamanlı işlem
    factorial_list[0] = 0  # 0! = 1 için özel kullanım, sabit zamanlı işlem (O(1))

    # 1'den 12'ye kadar tüm faktöriyel değerlerini hesapla
    for i in range(1, 13):  # O(n) zaman karmaşıklığı - n = 12
        result = result * i  # Her adımda çarpım işlemi (O(1))
        factorial_list[i] = result  # Hesaplanan değeri listeye kaydet (O(1))


# Önceden hesaplanmış faktöriyel değerini döndüren fonksiyon
def fact(n):
    # Listeye doğrudan erişim (O(1) zaman karmaşıklığı)
    return factorial_list[n]


# Faktöriyel değerlerini hesapla (O(n))
calculatefact()

# Test çalıştırmaları
print(fact(3))  # 3! = 6
print(fact(8))  # 8! = 40320
print(fact(12))  # 12! = 479001600

# Big-O Analizi:
# calculatefact() fonksiyonu:
# - Zaman Karmaşıklığı: O(n), n = 12
# - Alan Karmaşıklığı: O(n), factorial_list için n elemanlı liste
#
# fact(n) fonksiyonu:
# - Zaman Karmaşıklığı: O(1), listeye sabit zamanlı erişim
# - Alan Karmaşıklığı: O(1), ekstra alan kullanılmıyor
#
# Genel Analiz:
# - İlk hesaplama (calculatefact): O(n)
# - Her sorgu (fact): O(1)
