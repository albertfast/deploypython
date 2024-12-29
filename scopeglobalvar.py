def getAnswer():  
    result = "" #step 1

    while True:  #step 2 
       result = input("Your answer [yes/no]: ")
       if result == "yes":

         break 
       if result == "no":

         break 
       print("Let's try this again.")
    return result #step 3

def outputName(): 
     print("What is your name?")
     name = input()
     print("Thank you for telling me your name is", name)
     #outputName ends here
     return name
outputName()
def myfunc(text, num):
    while num > 0:
        num = num - 1

num = 4
myfunc('Hello', num)

# Print the value of num after calling the function
print(f"The value of num after the function call is: {num}")


# First function f(x), this increments the local x and prints it
def f(x):
    x = x + 1  # Local x is incremented by 1, so x becomes 4
    print('in f(x): x =', x, "(This is the local x inside the function, incremented by 1)")
    return x

x = 3  # Global x is defined as 3
z = f(x)  # Call the function f with x = 3 (global x doesn't change)
print(x, "(This is the global x, unchanged after calling f(x))")  # Output should be 3

# Second function f(y), demonstrating local variable usage
def f(y):
    x = 1  # Local x defined within f(), not related to global x
    x += 1  # Increment local x, now x = 2
    print(x, "(This is the local x inside the second f() function, set to 1 and incremented)")

x = 5  # Global x is now 5
f(x)  # Call f(x), but local x inside f() is different from global x
print(x, "(This is the global x, unchanged because f() does not modify global x)")  # Output should be 5

# Function g(y), which uses the global x
def g(y):
    print(x, "(This is the global x inside g(), output should be 5)")  # Prints the global x (5)
    print(x + 1, "(This is the global x + 1, so output should be 6)")  # Adds 1 to the global x, outputs 6

g(x)  # Call g(x), prints global x and x+1
print(x, "(This is still the global x, unchanged because g() does not modify it)")  # Output should be 5

# Function h(y), trying to modify x without declaring it as global (will cause an error)
def h(y):
    x += 1  # This would raise an error because x is not declared as global or initialized inside the function

x = 5  # Global x
# Uncommenting h(x) below would result in an error since it tries to modify x without declaring global
# h(x)  # This will raise an error if run
# print(x)  # This won't run if h(x) raises an error

'''
def getGrade():
# step 1
   result = 'X' # the default value

# step 2
   while True:
       result = input("What is your grade? [A, B, C, D, F, or X to quit]: ")[0]

       if result == 'A' or result == 'B' or result == 'C':
         break
       if result == 'D' or result == 'F':
         break
       if result == 'X' or result == 'x':
         break
       print(result, "is not a valid grade. Try again...")

# step 3
   return result
# getGrade ends here



# main program starts here
while True:
     grade = getGrade() # calling the getGrade() function inside the main program
     if grade != 'A' or grade == 'a' or grade != 'B' or grade == 'b':
        print("is not a valid grade. Try again...")
        break
     if grade == 'A' or grade == 'B' or grade == 'C':
         print("You pass")
print("Thanks for checking your grades!")
'''

''' 
def get_grade():
    """
    Prompts the user to enter a grade and returns it.
    """
    valid_grades = ['A', 'B', 'C', 'D', 'F', 'X']
    while True:
        grade = input("What is your grade? [A, B, C, D, F, or X to quit]: ").upper()
        if grade in valid_grades:
            return grade
        print(f"{grade} is not a valid grade. Try again...")


def main():
    while True:
        grade = get_grade()
        if grade in ['A', 'B', 'C']:
            print("You pass")
            break
        elif grade in ['D', 'F']:
            print("You do not pass")
            break
        elif grade == 'X':
            break
    print("Thanks for checking your grades!")


main()
'''
'''
import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()          # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()        # create alex
drawSquare(alex, 50)          # Call the function to draw the square

alex.penup()
alex.goto(100,100)
alex.pendown()

drawSquare(alex,75)           # Draw another square

'''
