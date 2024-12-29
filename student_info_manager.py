# Initialize the student dictionary with empty strings for each key.
# This dictionary will store student information with "first name", "last name", and "student_id" as initial keys.
student = {"first name": "", "last name": "", "student_id": ""}

# Prompt user to enter initial values for each key in the student dictionary.
# Using a for loop to iterate through each predefined key and ask the user for input.
for key in student.keys():
    student[key] = input(f"Enter {key}: ")

# Start a loop that allows the user to add more information to the dictionary.
# This loop will continue as long as the user wants to keep adding new entries.
while True:
    # Print the current state of the student information with each key-value pair displayed.
    # Adding a newline at the beginning makes the output more readable and separates updates.
    print("\nUpdated student information:")
    for key, value in student.items():
        print(f"{key}: {value}")

    # Ask the user if they want to add more information to the dictionary.
    # If the user enters 'Y' or 'y', they will be prompted to add a new key and value.
    # If they enter anything else, the loop will break and no more entries will be added.
    more = input("\nAdd more to the dictionary (Y or y for yes): ")
    if more.lower() != 'y':
        break

    # Prompt the user to enter a new key and its associated value.
    # This allows for flexible additions to the student dictionary, such as adding "age" or "email".
    key = input("\nEnter a kind of information to add: ")
    value = input("Enter the value for the information to add: ")
    student[key] = value  # Add the new key-value pair to the dictionary.

# Once the loop ends, print out the final dictionary contents.
# Display each key-value pair in the student dictionary for a complete summary.
print("\nFinal student information:")
for key, value in student.items():
    print(f"{key}: {value}")
