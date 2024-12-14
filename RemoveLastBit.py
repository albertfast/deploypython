# ================================UMPIRE========================================
# Understand:
# Given two input numbers, print out the two numbers with their
# binary value shifted to the right by 1 bit.
# Example    Input:        Output:
#            3 5           1 2
#            6 8           3 4
#            5 8           2 4
# Note ==> How we extract LSB ==>
# Option 1 ==> lsb = int % 2
# Option 2 ==> num_bin = bin(int here)
#              lsb = num_bin[-1]
# Option 3 ==> lsb = int & 1
# Match: Compare Last Bit, bitwise
# Plan



n1 = input()
lst_user_input = n1.split()
lsb_1 = int(lst_user_input[0])
lsb_2 = int(lst_user_input[-1])
print(lsb_1>>1, lsb_2>>1)
print(lsb_1 // 2, lsb_2 // 2)

lsb_1_bin = bin(lsb_1)
lsb_2_bin = bin(lsb_2)
print("lsb bins == ",lsb_1_bin, lsb_2_bin) # Output = 0b11 0b101 (for Input = 3 5)
# extract1 = lsb_1_bin[-1]
# extract2 = lsb_2_bin[len(lsb_2_bin)-1]
# print(extract1, extract2) # Output  # 1 1

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
