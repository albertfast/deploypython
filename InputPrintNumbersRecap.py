# ======================================================UMPIRE==============================================================
# Understand:
# Problem Statement: Write a program that takes in the user's name, which is taken in as input in all lower-case characters.
# If the least significant bit of the ten's place digit of the ASCII representation of the last character of the name matches
# with the least significant bit of the one's place digit of the ASCII representation of the last character,
# print Lsb matches: <tens lsb> <ones lsb>, otherwise print Lsb does not match: <tens lsb> <ones lsb>.
# Example ==>         Input:                         Output:
# 1                   anita                    Lsb matches: 1 1 ('a' is the last character of the name, and the ASCII representation of 'a' is 97.
#                                              The lsb of 9 is 1 and the lsb of 7 is 1, therefore both lsbs match).
#
# 2                   richard                 Lsb matches: 0 0 ('d' is the last character of the name, and the ASCII representation of 'd' is 100.
#                                             The lsb of 0 is 0 and the lsb of 0 is 0, therefore both lsbs match).
#
# 3                   chloe                   Lsb does not match: 0 1 ('e' is the last character of the name, and the ASCII representation of 'e' is 101.
#                                             The lsb of 0 is 0 and the lsb of 1 is 1, therefore both lsbs do not match).
#
# 4                   michael                 Lsb matches: 0 0
# 5                   ritu                    Lsb matches: 1 1
# 6                   edgar                   Lsb does not match: 1 0

# Restriction : lower case

# Match: Excel Sheet Column Number , Lsb >>

# Plan:
# 1. Take User input
# 2. Take last index value last_char = name[-1]
# 3. Find ASCII for last character ascii_value = ord(last_char)     (num >> 1) & 1)  (num >> 2) & 1)
# 4. Extract the tens digit from the ASCII value using (ascii_value // 10) % 10.
# 4.1 Extract the ones digit from the ASCII value using ascii_value % 10.
# 5. Calculate the LSB of the tens digit using tens_digit & 1.
# 6. Calculate the LSB of the ones digit using ones_digit & 1
# 7. compare two lms
#   7.1 if math
#           print match
#    7.2  else:
#          print does not match

name = input("Enter a name in lowercase: ").lower()


last_char = name[-1]


ascii_value = ord(last_char)
print(ascii_value)
tens_digit = (ascii_value // 10) % 10
ones_digit = ascii_value % 10
lsb_tens = tens_digit & 1
lsb_1 = ones_digit & 1

if lsb_tens == lsb_1:
    print(f"Lsb matches: {lsb_tens} {lsb_1}. ('{last_char}' is the last character of the name, "
          f"and the ASCII representation of '{last_char}' is {ascii_value}. The lsb of {tens_digit} is {lsb_tens} "
          f"and the lsb of {ones_digit} is {lsb_1}, therefore both lsbs match).")
else:
    print("Lsb does not match: ", lsb_tens, lsb_1)



















































