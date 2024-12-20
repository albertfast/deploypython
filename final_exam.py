# while True:
#     try:
#         # Ask user for input
#         user_input = float(input("Enter a non-zero number: "))
#         if user_input == 0:  # Check if the number is zero
#             print("The number cannot be zero. Please try again.")
#         else:
#             # Checking if the number is positive or negative
#             if user_input > 0:
#                 print("The input number is a positive number.")
#             else:
#                 print("The input number is a negative number.")
#             break  # Exit the loop after valid input
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#         # Handle non-numeric input

# Create a lambda function and assign it to variable s
s = lambda a, b, c, d, e: (a + b + c + d + e) / 5

# The lambda function takes 5 arguments (a, b, c, d, e) and
# returns their sum divided by 5 (the average of the 5 arguments)

# Example of Usage:
# call the function with 5 arguments, and print the return value
print(s(1, 2, 3, 4, 5))
# Output: 3.0