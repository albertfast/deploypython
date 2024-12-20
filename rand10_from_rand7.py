''''
Given the API rand7() that generates a uniform random integer in the range [1, 7], write a function rand10()
that generates a uniform random integer in the range [1, 10].
You can only call the API rand7(), and you shouldn't call any other API.
Please do not use a language's built-in random API.
Each test case will have one internal argument n, the number of times that your
implemented function rand10() will be called while testing. Note that this is not an argument passed to rand10().
'''
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        # İlk adım: 1-49 aralığında rastgele bir sayı elde etmek
        # rand7() - 1 ifadesi ile 0-6 arası değerler elde ederiz.
        # (rand7() - 1) * 7 ifadesi ile 0, 7, 14, ... , 42 (7'nin katları) değerleri üretilir.
        # rand7() - 1 ile bir 0-6 aralığında rastgele bir sayı daha ekleyerek, 0-48 aralığını elde ederiz.
        # Böylece toplamda 49 sayı (0 ile 48 dahil) elde edilir.
        c = (rand7() - 1) * 7 + rand7() - 1

        # Eğer c değeri 40 veya daha büyükse, yeniden rand10()'u çağır.
        # Bu sayede sadece 0 ile 39 arasındaki değerlere odaklanmış oluruz (1 ile 40).
        # 1-40 aralığı, 10'a tam bölündüğü için eşit olasılıkla 1-10 arasında sayılar üretmemizi sağlar.
        # 41-48 aralığı tekrar çekilerek adil bir dağılım elde edilir.
        return self.rand10() if c >= 40 else (c % 10) + 1

        # Sonuç olarak, c % 10 ile 0-9 aralığında bir sayı elde edilir.
        # Bu değere 1 ekleyerek 1-10 arası bir sayıya dönüştürürüz.
