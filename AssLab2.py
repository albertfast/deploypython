# Lambda function to convert mph to km/h. This defines an anonymous function
# that takes miles per hour as input and returns the equivalent kilometers per hour.
mph_to_kmh = lambda mph: mph * 1.609344

# Get input from the user. Prompts the user to enter a speed in miles per hour
# and converts the input to an integer. We use an integer for simplicity, but
# a float could be used for more precise speed values.
input_mph = int(input("Enter speed in mph for converting to km/h: "))

# Convert the input speed to km/h using the lambda function. This calls our
# anonymous function, passing in the user-provided speed in mph, and stores
# the calculated km/h value in the 'converted_speed' variable.
converted_speed = mph_to_kmh(input_mph)

# Print the conversion result. This formats the output nicely using an f-string
# to display the original mph value and the calculated km/h equivalent.
print(f"{input_mph} mph is equal to {converted_speed} km/h")
