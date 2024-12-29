#Programming Concepts In Python by Robert Burns Exercises 5.2 About Lighthouses, v.2.0

import math # Import the math module to use the sqrt function

def calculate_visibility_distance():
    # Prompt the user for the height of the lighthouse and convert it to a float
    height = float(input("Enter the height of the lighthouse in feet: "))

    # Calculate the distance in miles that the lighthouse can be seen from
    # Using the formula: distance = sqrt(0.8 * height)
    distance_in_miles = math.sqrt(0.8 * height)

    # Round the calculated distance to the nearest whole number
    rounded_distance = round(distance_in_miles)
    
    # Output the result in a formatted string that reports both the input height
    # and the calculated visible distance
    print(f"A {height} foot tall lighthouse can be seen from {rounded_distance} miles away.")

# Call the function to execute the calculations and display the results
calculate_visibility_distance()    
