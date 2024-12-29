class Employee:
    """
    The Employee class stores an employee's name, old salary, and new salary.
    """
    def __init__(self, name, old, new):
        # This method sets up the employee's information when the object is created.
        # The "name" is the employee's name, "old" is the old salary, and "new" is the new salary.
        self.name = name # Store the employee's name
        self.old = old   # Store the employee's old salary
        self.new = new   # Store the employee's new salary

    def print_name(self):
        # This method prints the employee's name.
        print(f"Employee's Name: {self.name}")

    def print_old_salary(self):
        # This method prints the employee's old salary.
        print(f"Employee's Old Salary: {self.old}")


    def print_new_salary(self):
        # This method prints the employee's new salary.
        print(f"Employee's New Salary: {self.new}")
        

 # Example usage
if __name__ == "__main__":
    # Create an Employee object with name, old salary, and new salary
    employee = Employee("Ahmet Sahiner", 8000, 11000)

    # Use methods to display the employee's information
    employee.print_name()  # Output: Employee's Name: Jane Smith
    employee.print_old_salary()  # Output: Employee's Old Salary: 8000
    employee.print_new_salary()  # Output: Employee's New Salary: 11000
