def ulam_sequence(first, second, terms):
    # İlk iki terimi listeye ekleyelim
    sequence = [first, second]

    # İlk iki terim zaten mevcut, geriye kalan terimler için hesaplama yapalım
    while len(sequence) < terms:
        candidates = {}
        for i in range(len(sequence)):
            for j in range(i + 1, len(sequence)):
                # Yeni terimleri hesaplayalım
                total = sequence[i] + sequence[j]
                if total not in sequence:  # Aynı terimler eklenmesin
                    candidates[total] = candidates.get(total, 0) + 1

        # Sadece bir kez oluşan en küçük toplamı bul
        next_term = min(k for k, v in candidates.items() if v == 1)
        sequence.append(next_term)

    return sequence


# Kullanıcıdan giriş alalım
first = int(input("İlk terim: "))
second = int(input("İkinci terim: "))
terms = int(input("Terim sayısı: "))

# Sonucu hesaplayalım ve yazdıralım
result = ulam_sequence(first, second, terms)
print(f"Ulam dizisi: {result}")
