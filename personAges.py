# Define the Human class
class Human:
    def __init__(self):
        self.name = None  # Attribute to store the name of the person
        self.age = None   # Attribute to store the age of the person

    def set_name(self, name):
        self.name = name  # Method to set the name attribute

    def set_age(self, age):
        self.age = age  # Method to set the age attribute

    def get_age(self):
        return self.age  # Method to retrieve the age attribute

# Define the Youth class inheriting from Human
class Youth(Human):
    """This class inherits from Human and specializes the behavior for Youth"""
    def age_appropriate(self):
        """Determines the message based on the age of the Youth"""
        if self.get_age() >= 18:
            print("You're old for a Youth!\n")  # If age is 18 or greater, print this message
        else:
            print("Nice to meet you young person.\n")  # Otherwise, print this message
# Define the Elder class inheriting from Human
class Elder(Human):
    # This class inherits from Human and specializes the behavior for Elder
    def age_appropriate(self):
        """Determines the message based on the age of the Elder"""
        if self.get_age() < 70:
            print("You're young for an Elder!\n")  # If age is less than 70, print this message
        else:
            print("Nice to meet you most venerable Senior.\n")  # Otherwise, print this message
def main():
    """
    This program demonstrates the following objectives:
    1. Learn how to put inheritance into classes and use inheritance when programming with objects:
       - The Human class serves as a base class with shared attributes and methods.
       - The Youth and Elder classes inherit from the Human class and reuse its attributes and methods.
       - Each derived class overrides the age_appropriate method to implement specialized behavior.

    2. Demonstrate a basic example of polymorphism:
       - A single object variable (person) is reused to represent instances of both Youth and Elder classes.
       - The age_appropriate method exhibits polymorphism by behaving differently depending on the actual class of the person object.

    This program dynamically determines the appropriate class (Youth or Elder) based on the user's input and executes the corresponding behavior.
    """
    person = None  # Initialize a single object variable
    print("\nWhenever want to leave the Application just type 'exit' to quit\n")
    while True:
        # Prompt the user for an age
        print("Enter an age for the person: ", end="")
        user_input = input()  # Take input from the user
        # Exit condition
        if user_input.lower() == 'exit':
            print("Exiting program. Goodbye!")  # Print exit message and break the loop
            break
        # Ensure input is numeric
        if user_input.isdigit():
            age = int(user_input)  # Convert the input to an integer
            # Assign person based on age and use age_appropriate
            if age <= 20:
                # If age is less than or equal to 20, assign person as a Youth
                person = Youth()  # Create a Youth object
                person.set_age(age)  # Set the age of the person
                person.age_appropriate()  # Call the age-appropriate method
            else:
                # If age is grater than 21 assign person as an Elder
                person = Elder()  # Create an Elder object
                person.set_age(age)  # Set the age of the person
                person.age_appropriate()  # Call the age-appropriate method
        else:
            # If input is not numeric, ask the user to enter a valid number
            print("Please enter a valid age as a number.\n")
# Run the program
if __name__ == "__main__":
    main()