# Selection
#total >= 60 ==> Pass
#total < 60 ==> No Pass

#while True:
    #try:
        #total = int(input())
    #except ValueError:
        #print("Invalid input, please enter a valid integer.")
        #continue
    #if total >= 60:
        #print('You Pass')
        #break
    #elif total < 60:
        #print('You Fail')
        #break
total = int(input())
grade = ""
if total >= 60:
    grade = "Pass"
else:
    grade = "No Pass"
print(grade)

#if Boolean expression:
#    <statement(s)>
#else:
#   <statement(s)>

#Syntax unary selection
#if Boolean expression:
#    <statement(s)>
total = 50
grade = "No Pass"
if total >= 60:
    grade = "Pass"

print(grade)

# Condition        Grade
# total >= 90        A
# 80 <= total < 90   B
# 70 <= total < 80   C
# 60 <= total < 70   D
#total < 60          F

total = 80
grade = ""

if total >= 90:
    grade = "A"
else:
    if total >= 80:
        grade = "B"
    else:
        if total >= 70:
            grade = "C"
        else:
            if total >= 60:
                grade = "D"
            else:
                grade = "F"
print(grade)

total = int(input())
grade = ""
if total >= 90:
    grade = "A"
elif total >= 80:
    grade = "B"
elif total >= 70:
    grade = "C"
elif total >= 60:
    grade = "D"
else:
    grade = "F"
print(grade)

#Scores of 90 or higher receive an A
#Scores of 80 or higher receive a B
#Scores of 70 or higher receive a C
#Scores of 60 or higher receive a D
#Any lower scores receive an F
score = int(input())
if score >= 90:
   print('A\n', 'PASS')
elif score >= 80:
   print('B\n', 'PASS')
elif score >= 70:
   print('C\n', 'PASS')
elif score >= 60:
   print('D\n', 'FAIL')
else:
   print('F\n', 'FAIL')














