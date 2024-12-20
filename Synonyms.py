# Understand:
# You are given a dictionary consisting of word pairs. Every word is a synonym of the other word in its pair.
# All the words in the dictionary are different.
# After the dictionary there's one more word given. Find a synonym for it.
# Example:    Input:               Output:
#             3
#             Hello Hi
#             Bye Goodbye           Bye
#             List Array
#             Goodbye
def build_synonyms(n):
    """Kullanıcıdan n adet kelime çifti alır ve eş anlamlılar sözlüğü oluşturur."""
    synonyms = {}
    for _ in range(n):
        word1, word2 = input().split()
        synonyms[word1] = word2
        synonyms[word2] = word1
    return synonyms

def find_synonym(synonyms, query):
    """Verilen kelimenin eş anlamlısını sözlükten döndürür."""
    return synonyms.get(query, "Eş anlamlı bulunamadı")  # Eğer kelime bulunamazsa bir mesaj döner

# Kullanıcıdan giriş al
n = int(input("Kaç çift kelime olacak? "))
synonyms_dict = build_synonyms(n)

query = input("Eş anlamlısını bulmak istediğiniz kelimeyi girin: ")
print(find_synonym(synonyms_dict, query))

#####################################
# Most Frequent Word
# Understand:
# Given the text: the first line contains the number of lines, then given the lines of words.
# Print the word in the text that occurs most often.
# If there are many such words, print the one that is less in the alphabetical order.
# Example:    Input:                  Output:
#             2
#             apple orange banana     banana
#             banana orange

# Implementation:

def most_frequent_word():
    # İlk satırda kaç satır olduğunu al
    n = int(input())
    word_counts = {}

    # n satır için giriş al
    for _ in range(n):
        line = input().split()
        for word in line:
            # Kelimenin frekansını artır
            word_counts[word] = word_counts.get(word, 0) + 1

    # En sık geçen kelimeleri bul
    max_frequency = max(word_counts.values())
    most_frequent_words = [word for word, count in word_counts.items() if count == max_frequency]

    # Alfabetik sıralama yap ve ilk kelimeyi seç
    result = sorted(most_frequent_words)[0]
    print(result)

# Fonksiyonu çalıştır
most_frequent_word()
































