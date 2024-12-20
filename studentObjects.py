class Student:
    """
    Class to represent a Student with personal details.
    Includes methods to initialize, input, and print student information.
    """
    def __init__(self, name=None, address=None, city=None, state=None, zip_code=None, student_id=None, gpa=None):
        """
          The __init__ method is a special method in Python classes, also known as a constructor.
    
          self: This is a reference to the current instance of the class. It is used to access variables that belong to the class. It must be the first parameter of any function in the class.
    
          __init__: This method is automatically called when a new instance of the class is created. It initializes the attributes of the class with the given arguments at the time of object creation.
    
          None: These are default values assigned to parameters. This means that if no value is provided for a parameter during object creation, it will default to None.
          This is used to facilitate flexible object creation without requiring all attributes to be set immediately.
        """
        # Initialize student attributes with provided or default (None) values
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code
        self.student_id = student_id
        self.gpa = gpa
        self.valid = True  # Indicates if the student data is valid

    def getInput(self, student_number):
        """
        Collects input from the user for this specific student object.
        Includes validation and error handling.
        """
        # Collect and validate input for each attribute
        self.name = self._get_valid_input(f"\nEnter for Student {student_number} Name", to_title=True, min_words=2, only_letters=True)
        if not self.name:
            return False

        self.address = self._get_valid_input("Address", to_title=True)
        if not self.address:
            return False

        self.city = self._get_valid_input("City", to_title=True, only_letters=True)
        if not self.city:
            return False

        self.state = self._get_valid_input("State", to_upper=True, only_letters=True, fixed_length=2)
        if not self.state:
            return False

        self.zip = self._get_valid_input("ZIP Code", is_numeric=True, fixed_length=5)
        if not self.zip:
            return False

        self.student_id = self._get_valid_input("Student ID", allow_alphanumeric=True, no_spaces=True)
        if not self.student_id:
            return False

        self.gpa = self._get_valid_gpa()
        if self.gpa is None:
            return False

        return True

    def printOutput(self):
        """
        Prints the student's details in a nicely formatted manner.
        If partial data is available, it prints only the provided fields.
        """
        # Print available student information; flag if data entry was incomplete
        if not self.valid:
            print("Partial data available for this student:")
        if self.name:
            print(f"Name: {self.name}")
        if self.address:
            print(f"Address: {self.address}")
        if self.city:
            print(f"City: {self.city}")
        if self.state:
            print(f"State: {self.state}")
        if self.zip:
            print(f"ZIP Code: {self.zip}")
        if self.student_id:
            print(f"Student ID: {self.student_id}")
        if self.gpa is not None:
            print(f"GPA: {float(self.gpa):.2f}")
        elif not any([self.name, self.address, self.city, self.state, self.zip, self.student_id]):
            print("No data available for this student.")  # Only print if all fields are None

    def _get_valid_input(self, prompt, to_title=False, to_upper=False, is_numeric=False, allow_alphanumeric=False,
                         only_letters=False, no_spaces=False, fixed_length=None, min_words=0):
        """
        A helper method to get validated input from the user.
        Returns user input after validation and transformation.
        """
        # An infinite loop to keep asking for input until valid data is received
        while True:
            user_input = input(f"{prompt}: ").strip()  # Prompt for input and remove leading/trailing spaces

            # Check if user wants to exit the input process
            if user_input.lower() == "exit":
                self.valid = False  # Mark the state as invalid to signal exit intention
                return None  # Exit this function returning None to stop data input

            # Validate if numeric input is needed with specific length if specified
            if is_numeric and (
                    not user_input.isdigit() or (fixed_length is not None and len(user_input) != fixed_length)):
                print(f"Invalid input. Please enter a numeric value of length {fixed_length}.")
                continue  # Prompt again for valid input

            # Validate alphanumeric input with optional prohibition of spaces
            if allow_alphanumeric and (not user_input.replace(" ", "").isalnum() or (no_spaces and " " in user_input)):
                print("Invalid input. Only letters and numbers are allowed, without spaces.")
                continue  # Prompt again for valid input

            # Validate input containing only letters (and spaces) with fixed length if specified
            if only_letters and (not all(c.isalpha() or c.isspace() for c in user_input) or (
                    fixed_length is not None and len(user_input) != fixed_length)):
                print(f"Invalid input. Only letters and spaces are allowed, with length {fixed_length}.")
                continue  # Prompt again for valid input

            # Verify that the input contains a minimum number of words
            if min_words > 0 and len(user_input.split()) < min_words:
                print(f"Invalid input. Please enter at least {min_words} words.")
                continue  # Prompt again for valid input

            # Transform input to title case if specified
            if to_title:
                return user_input.title()

            # Transform input to upper case if specified
            if to_upper:
                return user_input.upper()

            # If all validations pass, return the user input
            return user_input

    def _get_valid_gpa(self):
        """
        A helper method to validate GPA input.
        Ensures the GPA is between 0.0 and 4.0 and returns the value.
        """
        while True:
            gpa_input = input("GPA: ").strip()
            if gpa_input.lower() == "exit":
                self.valid = False
                return None
            try:
                gpa = float(gpa_input)
                if 0.0 <= gpa <= 4.0:
                    return gpa
                print("GPA must be between 0.0 and 4.0.")
            except ValueError:
                print("Invalid input. Please enter a valid GPA.")

# If you wish to quickly access the hardcoding test, comment out the relevant sections up to the help section,
# and then remove any dot notation used.
# Main Program
# Start the program by greeting the user
print("\nWelcome to the Student Management System!\nType 'exit' to quit at any time.")

# Create a list of 3 uninitialized Student objects
students = [Student() for _ in range(3)]

# Gather input for each student, allowing the user to exit early
for i, student in enumerate(students, start=1):
    if not student.getInput(i):
        print("\nUser chose to exit. Printing collected data...\n")
        break

# Print out the information for each student
print("==== Students Information ====")
for idx, student in enumerate(students, start=1):
    print(f"\n===== Student {idx} Details ======")
    student.printOutput()

#help(students)

"""
# Test Main Program
# Initial student data to be used for the first student
print("\nWelcome to the Student Management System!")
initial_student = {
    "name": "Albert Python",  # Default name for the first student
    "address": "123 main st.",  # Default address for the first student
    "city": "San Francisco",  # Default city for the first student
    "state": "CA",  # Default state for the first student
    "zip_code": "96358",  # Default ZIP code for the first student
    "student_id": "W2535",  # Default student ID for the first student
    "gpa": 4,  # Default GPA for the first student
}

# Dynamically generating test data for multiple students
test_data = [
    {
        "name": f"Student {i} Name" if i > 1 else initial_student["name"],  # Name is dynamic for students 2 and beyond
        "address": f"Address {i}" if i > 1 else initial_student["address"],  # Address is dynamic for students 2 and beyond
        "city": f"City {i}" if i > 1 else initial_student["city"],  # City is dynamic for students 2 and beyond
        "state": "CA",  # State remains the same for all students
        "zip_code": f"9000{i}" if i > 1 else initial_student["zip_code"],  # ZIP code changes based on the student index
        "student_id": f"S{i}ID" if i > 1 else initial_student["student_id"],  # Student ID is dynamic for students 2 and beyond
        "gpa": 3.5 + (i - 1) * 0.1 if i > 1 else initial_student["gpa"],  # GPA increments by 0.1 for students 2 and beyond
    }
    for i in range(1, 4)  # Generate data for 3 students
]

# Create Student objects from the test data
students = [Student(**data) for data in test_data]

# Print information for all students
print("==== Students Information ====")  # Header for the student information section
for idx, student in enumerate(students, start=1):

    print(f"\n===== Student {idx} Details ======")  # Header for each student's details
    student.printOutput()  # Print the formatted details of each student

#help(student)
# Access a specific attribute of a specific object
print(f"\nStudent 3's ID: {students[-1].student_id}")
# Print the reverse of Student 3's ID
print(f"\nStudent 2's ID reversed: {students[1].student_id[::-1]}")
"""
