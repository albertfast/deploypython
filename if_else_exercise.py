print("What is x value? ", end="")
x= int(input())

print("What is y value? ", end="")
y= int(input())

if x > y:
    print("Value of x greater than y")
elif y > x:
    print("Value of y greater than x")
else:
    print("Value of x and y must be equal")
    
