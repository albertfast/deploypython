# Prompt the user to enter their age (integer variable)
while True:
    try:
        age = int(input("How old are you? "))  # Attempt to convert the input to an integer
        break  # If successful, exit the loop
    except ValueError:
        print("Invalid input. Please enter a valid integer for your age.")  # If there's an error, prompt the user again

# Prompt the user to enter their birth weight (floating point variable)
print("What is your birth weight? ", end="")
birthWeight = float(input())  # Convert the input to a float and store it in the 'birthWeight' variable

# Prompt the user to enter their first name (multi-character text variable)
while True:
    firstName = input("What is your first name? ")  # Store the input as a string
    if len(firstName) > 1 and firstName.isalpha():
        break  # If the input is valid, exit the loop
    else:
        print("Invalid input. Please enter a name with more than 1 character and only letters.")

# Prompt the user to confirm if they are a computer programming student (1-character text variable)
print("Are you a computer programming student? (Y/N) ", end="")
isAComputerProgrammingStudent_input = input().upper()  # Convert the input to uppercase to handle both 'Y' and 'N'

# Determine if the user is a computer programming student and store the result
if isAComputerProgrammingStudent_input == "Y":
    isAComputerProgrammingStudent = f"Yes, I am a computer programming student ({isAComputerProgrammingStudent_input})"
elif isAComputerProgrammingStudent_input == "N":
    isAComputerProgrammingStudent = f"No, I am not a computer programming student ({isAComputerProgrammingStudent_input})"
else:
    isAComputerProgrammingStudent = "Invalid input. Please enter Y or N."


# Output all the values with appropriate labels
print(f"My age is {age}")  # Print the user's age
print(f"My birth weight is {birthWeight}") # Output the user's birth weight with a label
print(f"My first name is {firstName}") # Output the user's first name with a label
print(isAComputerProgrammingStudent) # Output the user's computer programming student status
