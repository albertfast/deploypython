import heapq  # heapq modülünü import ediyoruz (min-heap için)
import os

def runningMedian(a):
    """
    Verilen bir sayı dizisinin medyanını hesaplayan ve her yeni sayı eklendiğinde medyanı güncelleyen fonksiyon.

    Args:
        a: Bir sayı dizisi (list of integers).

    Returns:
        Her ekleme sonrası hesaplanan medyanların listesi (list of floats).
    """
    lowers = []  # max-heap (küçük elemanlar için, en büyük eleman üstte)
    highers = []  # min-heap (büyük elemanlar için, en küçük eleman üstte)
    medians = []  # Her eklemeden sonra hesaplanan medyanların listesi

    for num in a:  # Verilen sayı dizisinde dolaşıyoruz
        if not lowers or num <= -lowers[0]:
            # Eğer lowers heap'i boşsa veya sayı lowers'taki en büyük elemandan küçük veya eşitse lowers heap'ine ekle
            heapq.heappush(lowers, -num)  # lowers'a negatif eklenir (max-heap yapmak için)
        else:
             # Aksi durumda, sayıyı highers heap'ine ekle
            heapq.heappush(highers, num)

        # İki heap arasındaki dengeyi koruma:
        if len(lowers) > len(highers) + 1:
              # Eğer lowers heap'i highers'dan 1'den fazla büyükse, lowers'tan en büyük elemanı highers'a taşı
            heapq.heappush(highers, -heapq.heappop(lowers))
        elif len(highers) > len(lowers):
             # Eğer highers heap'i lowers'tan büyükse, highers'tan en küçük elemanı lowers'a taşı
            heapq.heappush(lowers, -heapq.heappop(highers))

        # Medyanı hesaplama:
        if len(lowers) == len(highers):
           # Eğer lowers ve highers aynı boyuttaysa, medyan iki heap'in tepe noktalarının ortalaması
            median = (-lowers[0] + highers[0]) / 2
        else:
             # Aksi takdirde, medyan lowers heap'inin tepe noktası
            median = -lowers[0]

        medians.append(float(f"{median:.1f}")) #Medyanı listeye ekler

    return medians # Medyanların listesini geri döndürür

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()