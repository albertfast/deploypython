# Create an empty list to store the ages
age_list = []

# Prompt the user to enter their age and add it to the list
print("What is your age? ", end = "")
age = int(input())
age_list.append(age)

# Prompt the user to enter their father's age and add it to the list
print("What is your father age? ", end = "")
age_father = int(input())
age_list.append(age_father)

# Prompt the user to enter their mother's age and add it to the list
print("What is your Mother age? ", end = "")
age_mother = int(input())
age_list.append(age_mother)

# Calculate the average age
average_age = sum(age_list) / len(age_list)

# Round the average age to the nearest whole number
rounded_age = round(average_age)

# Print the average age
print(f"Your family's age average is: {average_age:.2f}")

# Print the rounded average age
print(f"Your family's rounded age average is: {rounded_age}")
