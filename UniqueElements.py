def get_unique_elements(a_list):
    # Benzersiz elemanları bulmak için boş bir liste başlat
    unique_elements = []
    #  return [num for num in a_list if a_list.count(num) == 1]
    # Her eleman için frekans kontrolü yap
    for num in a_list:
        if a_list.count(num) == 1:  # Eğer eleman sadece bir kez geçiyorsa
            unique_elements.append(num)

    return unique_elements  # Benzersiz elemanları döndür


# Kullanıcıdan girdi al
a_list = [int(str_numbers) for str_numbers in input().split()]  # Girdi listesini oluştur
print(*get_unique_elements(a_list))  # Benzersiz elemanları yazdır
