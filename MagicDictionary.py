from typing import List
print(list(range(10)))
print(list("Python"))
class MagicDictionary:
    def __init__(self):
        # Boş bir kelime listesi başlatıyoruz
        self.words = []
        print("MagicDictionary initialized with an empty words list.")

    def buildDict(self, dictionary: List[str]) -> None:
        # Sözlükteki kelimeleri self.words listesine atıyoruz
        self.words = dictionary
        print(f"Dictionary built with words: {self.words}")

    def search(self, searchWord: str) -> bool:
        print(f"\nSearching for word: '{searchWord}'")
        
        for word in self.words:
            print(f"Comparing '{searchWord}' with '{word}'...")
            
            # Kelimenin uzunluğu searchWord ile aynı değilse devam et
            if len(word) != len(searchWord):
                print(f"Skipping '{word}' because length does not match.")
                continue
            
            # İki kelime arasındaki farklı karakter sayısını hesapla
            differences = sum(1 for i in range(len(word)) if word[i] != searchWord[i])
            print(f"Number of differing characters between '{searchWord}' and '{word}': {differences}")
            
            # Sadece 1 karakter fark varsa True döndür
            if differences == 1:
                print(f"Found a match with exactly one differing character: '{searchWord}' -> '{word}'")
                return True
        
        # Hiçbir eşleşme yoksa False döndür
        print(f"No matches found for '{searchWord}' with exactly one character difference.")
        return False

# Test adımları
md = MagicDictionary()
md.buildDict(["hello", "leetcode"])  # Sözlüğü oluşturuyoruz
print(md.search("hello"))  # Beklenen çıktı: False
print(md.search("hhllo"))  # Beklenen çıktı: True
print(md.search("hell"))   # Beklenen çıktı: False
print(md.search("leetcoded"))  # Beklenen çıktı: False
