import matplotlib.pyplot as plt

def process_number_with_for():
    user_input = int(input("Enter an integer: "))
    count = 0  # İşlem sayısını takip etmek için bir sayaç
    numbers = []  # Grafik için sayıları saklayacak liste

    print(f"Starting number: {user_input}")

    for i in range(1, 2000000):  # Döngü sınırını belirleyin
        numbers.append(user_input)  # Grafikte göstermek için sayıyı listeye ekle
        count += 1  # İşlem sayısını artır

        if user_input == 1:
            print(f"1 sonucuna {count} işlemde ulaşıldı.")
            break  # 1'e ulaşıldığında döngüyü durdur

        if user_input % 2 == 0:
            user_input = user_input // 2
        else:
            user_input = user_input * 3 + 1

    # Ulaşılan en büyük sayıyı bul
    max_value = max(numbers)
    max_index = numbers.index(max_value)

    # Grafik çizme
    plt.figure(figsize=(10, 6))
    plt.plot(numbers, marker='o', linestyle='-', color='b', label='Number Progression')
    plt.title(f"Collatz Conjecture Progression for {numbers[0]}", fontsize=14)
    plt.xlabel("Steps", fontsize=12)
    plt.ylabel("Number", fontsize=12)
    plt.legend()
    plt.grid(True)

    # Dinamik olarak ulaşılan işlem sayısını grafiğe ekle
    plt.annotate(f'Reached 1 in {count} steps',
                 xy=(len(numbers) - 1, numbers[-1]),  # En son noktaya yerleştir
                 xytext=(len(numbers) - 20, max(numbers) / 2),  # Daha iyi bir pozisyon için
                 arrowprops=dict(facecolor='red', shrink=0.05),
                 fontsize=12, color='red')

    # En büyük sayıyı grafikte işaretle
    plt.annotate(f'Max Value: {max_value}',
                 xy=(max_index, max_value),  # En büyük sayının olduğu noktaya yerleştir
                 xytext=(max_index + 10, max_value + max_value / 10),  # Daha iyi bir pozisyon için
                 arrowprops=dict(facecolor='green', shrink=0.05),
                 fontsize=12, color='green')

    plt.show()

if __name__ == "__main__":
    process_number_with_for()
