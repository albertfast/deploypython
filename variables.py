salaryJack = 5000
salaryAlbert = 4000
tax = 0.27

print(salaryJack - (salaryJack * tax))
print(salaryAlbert - (salaryAlbert * tax))

# Degisken Tanimlama Kurallari
# rakam ile baslayamaz  # 1number = 10 boyle yapilamaz
number1 = 40
number2 = 20
print(number1)
print(number2)
number1 += number2
print(number1)
number1 += 100
print(number1)

# Buyuk kucuk harf duyarliligi vardir

age = 25
AGE = 32

print(age)
print(AGE)

# Turkce karakter kullanmayalim

# x = 1
# y = 2.3
# name = "Albert"
# isStudent = True

x , y , name , isStudent = (2, 2.3, "Albert", True)
# 4 tane degiskene ayni anda atama yapmis olduk
print(x * y)
print(y)
print(name)
print(isStudent)

# Using a for loop without a list, by directly assigning questions and answers
for i in range(3):  # Looping for 3 questions
    if i == 0:
        question = "101 + 200 = "
        correct_answer = 101 + 200
    elif i == 1:
        question = "100 - (-29) = "
        correct_answer = 100 - (-29)
    elif i == 2:
        question = "-122 + 22 = "
        correct_answer = -122 + 22

    # While loop to handle user input
    while True:
        user_input = input(question)
        # Check if the input is a valid integer
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            if user_input == str(correct_answer):
                print("Congratulations – your answer is correct!\n")
                break  # Correct answer, exit the loop and move to the next question
            else:
                print(f"Nice try, but the correct answer is {correct_answer}.\n")
                break  # Incorrect answer, exit the loop and move to the next question
        else:
            print(f"'{user_input}' is an invalid input! Please enter a valid number.\n")

# Since all questions are complete
print("All calculations are complete!")
