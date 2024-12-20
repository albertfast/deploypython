# =====================Umpire===================
#Understand:
#Input = takes a single upper case letter (letter)
#Output =  position number in alphabet sequence.
#Restriction = upper case? single letter?
# A = 1, L = 12 , T = 20
# ord(letter) - ord('A') + 1

#Match: Excel Column Number (Two Letters): ord()

#Plan:
#1. Input Number
#2.  check upper case? single letter?
#3. take ord(letter) - ord('A') + 1
#4. print the sum position number in alphabet sequence

#Implementation:
while True:

    letter = str(input())
    if len(letter) == 1 and 'A' <= letter <= 'Z':
        print(ord(letter) - ord('A') + 1)
        break
    else:
        print('Invalid input. Please enter a single uppercase letter.')