# =====================Umpire===================
#Understand:
#Input = three-digit number
#Output = sum of digits
#Restriction = Can't use string operations
# 493 = 16
# 4 + 9 + 3 = 16
# 483 // 100 + (483 % 100 ) // 10 + 483 % 10 =16

#Match: Tens Digit: remainder and mod

#Plan:
#1. Input Number
#2. Extract 3rd digit
#3. Extract 2nd digit
#4. Extract 1st digit
#5. Sum all digits
#6. print the sum

#Implementation:
'''
while True:
    digits_three = int(input())
    if len(str(digits_three)) == 3:
        print(digits_three // 100 + (digits_three % 100) // 10 + digits_three % 10)
        break
    else:
        print("Invalid input. Please enter a 3-digit number like 589.")

year = int(input())
w_c = (year - 1) // 100
print(w_c)
c_c = (year - 1) //100 + 1
print(c_c)
'''
print(ord('A') - 64)
