# ======================================================UMPIRE==============================================================
# Understand:
#Given two input numbers, print 'True' if the last least significant bit of the two number match and 'False' if they don't.
# Note ==> How we extract LSB ==>
# Option 1 ==> lsb = int % 2
# Option 2 ==> num_bin = bin(int here)
#              lsb = num_bin[-1]
# Option 3 ==> lsb = int & 1
# n1, n2 = map(int, input().split())

# lsb_tens = n1 & 1
# lsb_1 = n2 & 1
#
# if lsb_tens == lsb_1:
#     print(True)
# else:
#     print(False)

n1 = input()
print(len(n1))
lst_user_input = n1.split()
print(lst_user_input)
lsb_1 = int(lst_user_input[0]) & 1
lsb_2 = int(lst_user_input[1]) & 1

if lsb_1 == lsb_2:
    print(True)
else:
    print(False)

# n1 = input()
# print(len(n1))
# lst_user_input = n1.split()
# print(lst_user_input)
# lsb_1 = lst_user_input[0]
# lsb_2 = lst_user_input[1]
# lsb_1_bin = bin(int(lsb_1))
# lsb_2_bin = bin(int(lsb_2))
# print(lsb_1, lsb_2)
# print(lsb_1_bin, lsb_2_bin) # Output = 0b11 0b101
# extract1 = lsb_1_bin[-1]
# extract2 = lsb_2_bin[len(lsb_2_bin)-1]
# print(extract1, extract2) # Output  # 1 1
