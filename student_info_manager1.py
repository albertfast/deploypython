# File: student_info1.py

def collect_student_info():
    """
    Collect student information interactively and return it as a dictionary.
    """
    # Initialize the student dictionary with empty strings for each key.
    student = {"first name": "", "last name": "", "student_id": ""}

    # Prompt user to enter initial values for each key in the student dictionary.
    for key in student.keys():
        student[key] = input(f"Enter {key}: ")

    # Start a loop that allows the user to add more information to the dictionary.
    while True:
        # Print the current state of the student information with each key-value pair displayed.
        print("\nUpdated student information:")
        for key, value in student.items():
            print(f"{key}: {value}")

        # Ask the user if they want to add more information to the dictionary.
        more = input("\nAdd more to the dictionary (Y or y for yes): ")
        if more.lower() != 'y':
            break

        # Prompt the user to enter a new key and its associated value.
        key = input("\nEnter a kind of information to add: ")
        value = input("Enter the value for the information to add: ")
        student[key] = value  # Add the new key-value pair to the dictionary.

    # Once the loop ends, print out the final dictionary contents.
    print("\nFinal student information:")
    for key, value in student.items():
        print(f"{key}: {value}")

    return student


# If the script is run directly, execute the function
if __name__ == "__main__":
    collect_student_info()
