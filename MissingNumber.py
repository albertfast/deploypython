# Understand:
# Given a list, nums, containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the list.
# Constraints:
# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
# Example ==>      Input:                       Output:
#                  [3, 0, 1]                    2
#                  [0, 1]                       2
#                  [9, 6, 4, 2, 3, 5, 7, 0, 1]  8

def missingNumber(nums):
    nums.sort()  # Listeyi sıralıyoruz
    low, high = 0, len(nums)

    while low < high:
        mid = (low + high) // 2
        if nums[mid] > mid:  # Eksik sayı sol tarafta
            high = mid
        else:  # Eksik sayı sağ tarafta
            low = mid + 1

    return low

print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))

def missingNumber2(nums):
    unique_nums = list(set(nums))
    n = len(unique_nums)
    expected_sum =  (n + 1) * (n + 2) // 2
    actual_sum = sum(unique_nums)
    return expected_sum - actual_sum
nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11, 13]
nums1 = [1, 2, 3, 4]

print(missingNumber2(nums))
print(missingNumber2(nums1))

def missingNumberWithLoop(integers):
    integers.sort()
    integers = list(set(integers))
    n = max(integers)

    for i in range(1, n + 1):
        if i not in integers:
            return i

    return n + 1
integers = [7, 14, 2, 3, 6, 4, 1, 5, 12, 0, 13, 9, 10, 11]
print("O(n log n) solution: ",missingNumberWithLoop(integers))

# Function to find the first missing positive integer in a sorted list
# Eğer giriş listesini sıralamak isterseniz, önce numbers.sort() çağrılmalıdır. Ancak, bu durum kodun zaman karmaşıklığını O(n log n) seviyesine çıkarır.
# Algoritmanın şu anki hali O(n) karmaşıklığındadır çünkü sadece bir döngü kullanır ve sıralama işlemi gerektirmez.
# Sıralı bir listede eksik olan ilk pozitif tam sayıyı bulma fonksiyonu
def find_first_missing_positive(numbers):
    # Loop through the input list to find the first mismatch between index and value
    # Giriş listesindeki index ve değer arasında eşleşmeyen ilk öğeyi bulmak için döngü
    for index in range(len(numbers)):  # O(n): Her elemanı bir kez kontrol eder
        # If the value at the current index does not match the index itself
        # Eğer mevcut indeksteki değer, indeksin kendisine eşit değilse
        if index != numbers[index]:
            return index  # Return the index as the missing number
            # Eksik olan sayıyı indeks olarak döndür

    # If all indices match their values, the missing number is the length of the list
    # Eğer tüm indeksler değerlerle eşleşiyorsa, eksik sayı listenin uzunluğudur
    return len(numbers)

# Test the function with an example input list
# Fonksiyonu bir örnek giriş listesiyle test et
input_numbers = [7, 14, 2, 3, 6, 4, 1, 5, 12, 0, 13, 9, 10, 11]
print("First missing positive integer (sorted): ", find_first_missing_positive(input_numbers))



# Function to find the first missing positive integer in a list
# Bir listedeki eksik ilk pozitif tamsayıyı bulmak için bir fonksiyon
def find_first_missing_positive(numbers):
    # Initialize a "seen" list with 0s to track presence of numbers
    # Sayıların varlığını takip etmek için sıfırlarla bir "görülen" listesi başlat
    seen = [0] * (len(numbers) + 1)  # O(n): "seen" listesi giriş boyutuna göre oluşturulur.

    # Mark the numbers that exist in the input list
    # Giriş listesindeki mevcut sayıları işaretle
    for num in numbers:  # O(n): Giriş listesindeki her sayı bir kez işlenir.
        if num < len(numbers) + 1:  # Ensure the number is within range
            # Sayının aralık içinde olduğundan emin ol
            seen[num] = 1  # Sayının var olduğunu işaretle.

    # Find the first index in the "seen" list that is still 0
    # Hala 0 olan "görülen" listesindeki ilk indeksi bul
    for index in range(len(seen)):  # O(n): "seen" listesindeki her indeks kontrol edilir.
        if seen[index] == 0:
            return index  # Eksik sayıyı döndür.

# Test the function
# Fonksiyonu test et
input_numbers = [7, 14, 2, 3, 6, 4, 1, 5, 12, 0, 13, 9, 10, 11]
print("First missing positive integer: ", find_first_missing_positive(input_numbers))


