# Prompt the user for two inputs
print("Enter the first number: ", end="")
input1 = int(input())  

print("Enter the second number: ", end="")
input2 = int(input())  

# Assign variable c as the sum of the two inputs
c = input1 + input2

# Assign variable d to the value 5
d = 5

# Use if-elif structure to handle different conditions
if c > d:
    print("Happy")
elif c == d:
    print("Glad")
elif (c + d) == 10:
    print("Wow")
elif c < d:
    # If c is less than d, print the value of c 50 times with an index
    for i in range(1, 51):  # Loop from 1 to 50
        print(f"{i}. {c}")
