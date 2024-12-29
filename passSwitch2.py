# Read a grade from the keyboard and convert to lowercase
grade = input("What is your grade? [A, B, C, D, or F]: ").lower()

# Check for passing or failing grades
if grade in ['a', 'b', 'c']:
    print("Really excellent work!")  # Output for passing grades
elif grade in ['d', 'f']:
    print("Yikes -- you failed...")  # Output for failing grades
else:
    print("No, that's an invalid entry")  # Output for invalid entries
