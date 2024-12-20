'''
n = int(input("Enter a number: "))
if n <= 0:
    print("please input a positive integer")
else:
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} FizzBuzz")
        elif i % 5 == 0:
            print(f"{i} Buzz")
        elif i % 3 == 0:
            print(f"{i} Fizz")
        else:
            print(f"{i}")
'''

class DivisibilityChecker:

    def __init__(self, n):

        self.n = n

    def check_divisibility(self):
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print(f"{i} FizzBuzz")
            elif i % 5 == 0:
                print(f"{i} Buzz")
            elif i % 3 == 0:
                print(f"{i} Fizz")
            else:
                print(f"{i}")
                
checker = DivisibilityChecker(33)

checker.check_divisibility()

'''
# Take the first number (input from the user)
n = int(input())

# Loop through numbers from 1 to n
for i in range(1, n + 1):
    # Check if it is divisible by both 3 and 5, if yes print 'FizzBuzz'
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Check if it is divisible by 3, if yes print 'Fizz'
    elif i % 3 == 0:
        print("Fizz")
    # Check if it is divisible by 5, if yes print 'Buzz'
    elif i % 5 == 0:
        print("Buzz")
    # If it is not divisible by either 3 or 5, print the number itself
    else:
        print(i)

'''


