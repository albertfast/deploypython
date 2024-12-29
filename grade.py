# read a score from the keyboard (see 5.2.1) 
grade = input("What is your grade? [A, B, C, D, or F]: ")
  
# check for passing grade 
if grade == 'A' or grade == 'B' or grade == 'C': 
  print("You pass") 
else:
  print("You do not pass")

# set a variable called userGuess from the user's input 
userGuess = int(input("Please type an integer number as a guess "))


# userGuess is in a conditional statement to be used over and over again  
# the conditional statement is a part of a while loop
if userGuess == 7:
    print("You know that!")
while userGuess != 7: 
  print("Could you please try again?")
  userGuess = int(input("Please type an integer number as a guess "))


