# ========================= STRINGLERLE İLGİLİ TÜM KONU BAŞLIKLARI ===========================
# Bu kod, Python'da string işlemleri ile ilgili temel ve ileri seviye konuları kapsar.
# String oluşturma, indeksleme, dilimleme, metotlar ve döngüler gibi konular işlenecek.

# ------------------------- STRING OLUŞTURMA -------------------------
# Stringler çift tırnak (" ") ya da tek tırnak (' ') ile oluşturulabilir.
string1 = "Merhaba, Dünya!"  # Çift tırnakla string
string2 = 'Python harika!'   # Tek tırnakla string

print("String 1:", string1)  # String 1: Merhaba, Dünya!
print("String 2:", string2)  # String 2: Python harika!

# Çok satırlı stringler üçlü tırnaklar kullanılarak yazılabilir.
multi_line_string = """Bu bir
çok satırlı
stringdir."""
print(multi_line_string)

# ------------------------- STRING İNDEKSLEME -------------------------
# Stringler indekslenebilir. İndeksler sıfırdan başlar.
string = "Python"
print("İlk harf:", string[0])  # P
print("Son harf:", string[-1]) # n

# ------------------------- STRING DİLİMLEME -------------------------
# String dilimleme, stringden belirli bir aralık almak için kullanılır.
print("İlk üç harf:", string[:3])  # Pyt
print("Son üç harf:", string[-3:]) # hon
print("2. ile 4. harf arası:", string[1:4])  # yth

# ------------------------- STRING BİRLEŞTİRME -------------------------
# İki stringi birleştirmek için + operatörü kullanılır.
string3 = "Python"
string4 = "Programlama"
birlesik_string = string3 + " " + string4
print("Birleştirilmiş String:", birlesik_string)  # Python Programlama

# ------------------------- STRING ÇARPMA -------------------------
# Bir stringi belirli bir sayıda tekrarlamak için * operatörü kullanılır.
print("Tekrarlı String:", string3 * 3)  # PythonPythonPython

# ------------------------- STRING METOTLARI -------------------------
# Stringlerde kullanabileceğimiz birçok yerleşik metot vardır.

# upper() ve lower(): Tüm harfleri büyük veya küçük yapar.
print("Büyük harf:", string3.upper())  # PYTHON
print("Küçük harf:", string3.lower())  # python

# strip(): Başındaki ve sonundaki boşlukları siler.
string5 = "   Python   "
print("Striplenmiş String:", string5.strip())  # "Python"

# replace(): Bir substring'i başka bir substring ile değiştirir.
print("Replace Örneği:", string4.replace("Programlama", "Kodlama"))  # Python Kodlama

# split(): Stringi belirli bir ayraca göre böler.
string6 = "Python,Java,C++"
diller = string6.split(",")
print("Bölünmüş String:", diller)  # ['Python', 'Java', 'C++']

# join(): Liste veya tuple'daki elemanları birleştirir.
birlesmis_string = " - ".join(diller)
print("Birleştirilmiş String:", birlesmis_string)  # Python - Java - C++

# find(): Belirtilen karakterin veya kelimenin indeksini döner.
print("Java'nın İndeksi:", string6.find("Java"))  # 7

# count(): Belirtilen karakterin kaç kez geçtiğini döner.
print("o Harfi Sayısı:", string3.count("o"))  # 1

# startswith() ve endswith(): Stringin belirli bir karakterle başlayıp bitip bitmediğini kontrol eder.
print("Python ile başlıyor mu?", string3.startswith("Python"))  # True
print("Dünya ile bitiyor mu?", string1.endswith("Dünya!"))  # True

# ------------------------- STRINGLERLE DÖNGÜLER -------------------------
# Bir stringin her bir karakterini döngü ile dolaşabiliriz.
for harf in string3:
    print(harf, end="-")  # P-y-t-h-o-n-
print()  # Bir satır boşluk

# ------------------------- STRING FORMATLAMA -------------------------
# F-string kullanarak değişkenleri stringlere kolayca ekleyebiliriz.
isim = "Ahmet"
yas = 25
print(f"Merhaba, benim adım {isim} ve {yas} yaşındayım.")  # Merhaba, benim adım Ahmet ve 25 yaşındayım.

# ------------------------- KARAKTERLERİ BÜYÜTME/KÜÇÜLTME -------------------------
# Dinamik olarak bir stringin harflerini büyük veya küçük yapmak.
string7 = "Merhaba Dünya"
yeni_string = ""
for harf in string7:
    if harf.islower():  # Eğer harf küçükse büyüt
        yeni_string += harf.upper()
    else:  # Eğer harf büyükse küçült
        yeni_string += harf.lower()
print("Değiştirilmiş String:", yeni_string)  # mERHABA dÜNYA

# ------------------------- DİNAMİK DEĞİŞİM -------------------------
# Kullanıcıdan hangi karakteri değiştirmek istediğini alalım.
original_char = input("Hangi karakteri değiştirmek istersiniz?: ")
replacement_char = input("Yerine ne koymak istersiniz?: ")
modified_string = string7.replace(original_char, replacement_char)
print("Değiştirilmiş String:", modified_string)

# ------------------------- TERS ÇEVİRME -------------------------
# Stringi ters çevirmek için [::-1] dilimleme kullanılır.
ters_string = string7[::-1]
print("Ters Çevrilmiş String:", ters_string)  # ay nüD abahreM

# ------------------------- STRING UZUNLUĞU -------------------------
# Stringin kaç karakterden oluştuğunu öğrenmek için len() fonksiyonu kullanılır.
print("String Uzunluğu:", len(string7))  # 13

# ------------------------- STRING KULLANIMI ÖZET -------------------------
# Yukarıda öğrendiklerimizi kullanarak bir özet:
ornek_string = "Python Programlama Dili Harika!"
print("Orijinal String:", ornek_string)
print("Küçük Harf:", ornek_string.lower())
print("Büyük Harf:", ornek_string.upper())
print("Kelime Sayısı:", len(ornek_string.split()))  # Boşluklara göre böler ve kelime sayısını verir.
print("Ters String:", ornek_string[::-1])

#-------------------------------3 e tam bolunen index cikart ------------------
# Kullanıcıdan bir string al
input_string = input("Bir string girin: ")

# Sonuç stringini başlat
result_string = ""

# Döngü ile stringdeki her karakteri ve indeksini al
for index, char in enumerate(input_string):
    # Eğer indeks 3'e tam bölünmüyorsa, karakteri ekle
    if index % 3 != 0:
        result_string += char

# Sonucu yazdır
print("Sonuç:", result_string)
