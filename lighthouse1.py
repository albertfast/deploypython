#Programming Concepts in Python 4.2
# Get the height of the lighthouse from the user without moving to a new line after the prompt.
print("Enter the height of the lighthouse in feet: " , end = "")
height = float(input())

# Calculate the distance in miles and round it to the nearest whole number.
distance_in_miles = (0.8 * height) ** 0.5
rounded_distance = round(distance_in_miles)

# Print the result in a formatted string that includes both the input height and the calculated distance.
# Here we use .0f to display the number with zero decimal places.
print(f"A {height:.0f} foot tall lighthouse can be seen from {rounded_distance} miles away.")

print("What is your age? ", end = "")
age = input()
print("This input age type is: ", type(age))
#What is your age? 36
#This input age type is:  <class 'str'>

print("What is your Father age? ", end = "")
father_age = int(input())
print("This input Father age type is: ", type(father_age))
#What is your Father age? 42
#This input Father age type is:  <class 'int'>

print("What is your favorite color? ", end = "")
color = input()
print("This input color type is: ", type(color))
#What is your favorite color? blue
#This input color type is:  <class 'str'>
