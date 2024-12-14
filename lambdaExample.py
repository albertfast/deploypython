# Python'da lambda ve def kullanımı ile matematiksel işlemler örnekleri

# Örnek 1: Lambda ile 3x + 1 işlemi
f1 = lambda x: 3 * x + 1
print("Örnek 1 - x = 2 için, 3x + 1 işleminin sonucu:", f1(2))  # Çıktı: 7
# Açıklama: Burada x değeri 2 iken, 3 * 2 + 1 işlemi yapılır ve sonuç 7 olarak bulunur.

# Örnek 2: Lambda ile iki sayının toplamı
topla = lambda a, b: a + b
print("Örnek 2 - a = 5 ve b = 3 için, a + b işleminin sonucu:", topla(5, 3))  # Çıktı: 8
# Açıklama: Burada a değeri 5, b değeri 3 iken, 5 + 3 işlemi yapılır ve sonuç 8 olur.

# Örnek 3: Lambda ile Koşullu İfade Kullanımı
kontrol = lambda x: "Pozitif" if x > 0 else "Negatif" if x < 0 else "Sıfır"
print("Örnek 3 - x = -4 için durum:", kontrol(-4))  # Çıktı: Negatif
# Açıklama: x değeri -4 olduğunda, negatif olduğu için sonuç "Negatif" olur.

# Örnek 4: def ile Fibonacci Serisi Hesaplama
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Örnek 4 - İlk 5 Fibonacci sayısı:")
for i in range(5):
    print(f"Fibonacci({i}):", fibonacci(i))
# Açıklama: Fibonacci serisindeki her sayı, kendisinden önceki iki sayının toplamıdır.

# Örnek 5: Lambda ile Üçgen Alanı Hesaplama
ucgen_alani = lambda taban, yukseklik: (taban * yukseklik) / 2
print("Örnek 5 - Taban = 10 ve Yükseklik = 5 olan üçgenin alanı:", ucgen_alani(10, 5))  # Çıktı: 25.0
# Açıklama: Üçgenin alanı (10 * 5) / 2 ile bulunur ve sonuç 25.0 olur.

# Örnek 6: def ile Sayının Faktöriyelini Hesaplama
def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n - 1)

print("Örnek 6 - 5'in faktöriyeli:", faktoriyel(5))  # Çıktı: 120
# Açıklama: 5! = 5 * 4 * 3 * 2 * 1 = 120 olarak hesaplanır.

# Örnek 7: Lambda ile İki Sayının Üssünü Almak
us_al = lambda a, b: a ** b
print("Örnek 7 - 2'nin 3. kuvveti:", us_al(2, 3))  # Çıktı: 8
# Açıklama: 2^3 işlemi yapılır, yani 2 * 2 * 2 = 8 olur.

# Örnek 8: Lambda ile İsim Birleştirme
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print("Örnek 8 - İsim Birleştirme:", full_name("  leonhard", "EULER"))  # Çıktı: 'Leonhard Euler'
# Açıklama: İsim ve soyadı birleştirilip baş harfleri büyük yapılır.

# Örnek 9: Lambda ile Mutlak Değer Hesaplama
mutlak_deger = lambda x: abs(x)
print("Örnek 9 - x = -7 için mutlak değer:", mutlak_deger(-7))  # Çıktı: 7
# Açıklama: -7'nin mutlak değeri 7'dir.

# Örnek 10: Lambda ile Sinüs Fonksiyonu (NumPy ile)
import math
sinus = lambda x: math.sin(x)
print("Örnek 10 - 90 derece (radyan olarak π/2) sinüsü:", sinus(math.pi / 2))  # Çıktı: 1.0
# Açıklama: 90 derece radyan olarak π/2'ye eşittir ve sin(π/2) = 1 olur.

# Önceki kodların altına eklemek için ek örnekler

# Örnek 11: def ile Tanımlanan Bir Fonksiyonu Lambda İçinde Çağırma
def kare(x):
    """Bu fonksiyon verilen sayının karesini alır."""
    return x ** 2

# Lambda içinde kare fonksiyonunu çağırıyoruz
kare_lambda = lambda x: kare(x)
print("Örnek 11 - def ile tanımlanan kare fonksiyonunu lambda içinde çağırma:", kare_lambda(5))  # Çıktı: 25
# Açıklama: kare(5) işlemi yapılır ve 5'in karesi 25 olarak döner.

# Örnek 12: Lambda ile Tanımlanan Bir İşlemi def Fonksiyonu İçinde Çağırma
kup_lambda = lambda x: x ** 3  # Lambda ifadesi ile küp alma işlemi

def hesapla_kup(x):
    """Lambda ifadesini kullanarak sayının küpünü hesaplar."""
    return kup_lambda(x)

print("Örnek 12 - lambda ile tanımlanan küp alma işlemini def içinde çağırma:", hesapla_kup(3))  # Çıktı: 27
# Açıklama: kup_lambda(3) çağrılır ve 3'ün küpü olan 27 sonucu elde edilir.

# Örnek 13: def ile İç İçe Fonksiyonlar Kullanarak Lambda Döndürme
def topla_carp(a, b):
    """Bu fonksiyon, iki sayıyı önce toplar, sonra çarpma işlemi için bir lambda döndürür."""
    toplam = a + b
    return lambda x: toplam * x

carpma_fonksiyonu = topla_carp(2, 3)
print("Örnek 13 - def ile iç içe fonksiyonlar ve lambda kullanımı:", carpma_fonksiyonu(4))  # Çıktı: 20
# Açıklama: topla_carp(2, 3) çağrıldığında toplam 5 olur ve lambda x: 5 * x döndürülür.
# carpma_fonksiyonu(4) ise 5 * 4 = 20 sonucunu verir.

# Örnek 14: Lambda ile Tanımlanan Birden Fazla İşlemi def İçinde Kullanma
# Lambda ifadeleri ile farklı işlemler tanımlıyoruz
toplama = lambda a, b: a + b
cikarma = lambda a, b: a - b
carpma = lambda a, b: a * b
bolme = lambda a, b: a / b if b != 0 else "Tanımsız"  # 0'a bölünme durumunda tanımsız döner

def islemler(a, b):
    """Lambda ifadeleri ile toplama, çıkarma, çarpma ve bölme işlemleri yapar."""
    print(f"Toplama ({a} + {b}):", toplama(a, b))
    print(f"Çıkarma ({a} - {b}):", cikarma(a, b))
    print(f"Çarpma ({a} * {b}):", carpma(a, b))
    print(f"Bölme ({a} / {b}):", bolme(a, b))

print("Örnek 14 - Lambda ile dört işlem")
islemler(10, 5)
# Açıklama: toplama, cikarma, carpma ve bolme lambda ifadeleri kullanılarak def içinde çağrılır.

# Örnek 15: def ve lambda İle Koşullu İşlem
def durum_mesaji(sayi):
    """Lambda ile koşullu işlem kullanarak pozitif, negatif veya sıfır durumunu kontrol eder."""
    kontrol = lambda x: "Pozitif" if x > 0 else "Negatif" if x < 0 else "Sıfır"
    return f"{sayi} sayısı {kontrol(sayi)}'dır."

print("Örnek 15 - def ve lambda ile koşullu işlem:", durum_mesaji(-10))  # Çıktı: -10 sayısı Negatif'tir.
# Açıklama: Lambda içinde koşullu ifade kullanarak sayının durumunu kontrol eder.

# Örnek 16: Lambda İle Bir def Fonksiyonunda Hesaplama Yapma
def tam_bolenler(sayi):
    """Verilen sayının tüm tam bölenlerini lambda kullanarak döndürür."""
    bolenler = list(filter(lambda x: sayi % x == 0, range(1, sayi + 1)))
    return bolenler

print("Örnek 16 - Lambda kullanarak tam bölenleri bulma:", tam_bolenler(12))  # Çıktı: [1, 2, 3, 4, 6, 12]
# Açıklama: Lambda ile, sayıyı tam bölen değerleri filtreleme işlemi yapıyoruz.

# Örnek 17: Lambda İle def İçinde Yüksek Mertebe Fonksiyonlar
def hesapla_ve_uygula(x, f):
    """Verilen fonksiyonu (f) x değerine uygular ve sonucu döndürür."""
    return f(x)

# Yüksek mertebe fonksiyonu lambda ile kullanıyoruz
print("Örnek 17 - Lambda ve def ile yüksek mertebe fonksiyon:", hesapla_ve_uygula(10, lambda x: x ** 2))  # Çıktı: 100
# Açıklama: hesapla_ve_uygula, x'in karesini alan lambda fonksiyonunu uyguluyor.

# Örnek 18: Lambda ve def Kullanarak Bir Dizide Filtreleme Yapma
sayilar = list(range(-10, 11))  # -10 ile 10 arası sayılar
pozitifler = list(filter(lambda x: x > 0, sayilar))  # Lambda ile pozitif sayıları filtreler
print("Örnek 18 - Lambda ile pozitif sayıları filtreleme:", pozitifler)  # Çıktı: [1, 2, ..., 10]
# Açıklama: Filter ve lambda kullanarak dizideki pozitif sayıları buluyoruz.

# Örnek 19: def Fonksiyonundan Birden Fazla Lambda Döndürme
def islemler_dondur():
    """Toplama ve çarpma işlemleri için lambda fonksiyonları döndürür."""
    return lambda a, b: a + b, lambda a, b: a * b

topla, carp = islemler_dondur()
print("Örnek 19 - def ile döndürülen lambda ile toplama:", topla(3, 4))  # Çıktı: 7
print("Örnek 19 - def ile döndürülen lambda ile çarpma:", carp(3, 4))  # Çıktı: 12
# Açıklama: islemler_dondur fonksiyonu, toplama ve çarpma işlemleri için lambda fonksiyonları döndürür.

# Örnek 20: def ve Lambda İle İsim Formatlama
def formatla(isim, soyisim):
    """İsim ve soyismi lambda ile formatlar."""
    full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
    return full_name(isim, soyisim)

print("Örnek 20 - Lambda ile isim formatlama:", formatla("   albert", "eInStEiN"))  # Çıktı: Albert Einstein
# Açıklama: Lambda, verilen ismi baş harfleri büyük olacak şekilde formatlar.
