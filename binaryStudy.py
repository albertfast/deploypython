n1 = input()  # Kullanıcıdan iki sayı al
lst_user_input = n1.split()  # Sayıları listeye çevir
lsb_1 = int(lst_user_input[0])  # İlk sayıyı integer yap
lsb_2 = int(lst_user_input[1])  # İkinci sayıyı integer yap
lsb_1_bin = bin(lsb_1)  # İlk sayının binary string temsili
lsb_2_bin = bin(lsb_2)  # İkinci sayının binary string temsili
bin_to_int1 = int(lsb_1_bin, 2)  # Binary string'i tekrar integer yap (Gereksiz çünkü zaten integer'dı)
bin_to_int2 = int(lsb_2_bin, 2)  # İkinci binary string'i tekrar integer yap
print(bin_to_int1 >> 1, bin_to_int2 >> 1)  # Right shift ile sonuçları yazdır
print("From input integer to binary ==>", lsb_1_bin, lsb_2_bin)
print("After bitwise newBinary      ==>" , bin(bin_to_int1 >> 1), bin(bin_to_int2 >> 1))


n1 = input()  # Kullanıcıdan iki sayı al
lst_user_input = n1.split()  # Sayıları listeye çevir
lsb_1 = int(lst_user_input[0])  # İlk sayıyı integer yap
lsb_2 = int(lst_user_input[1])  # İkinci sayıyı integer yap
print(lsb_1 >> 1, lsb_2 >> 1)  # Right shift ile sonuçları yazdır

