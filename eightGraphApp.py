import random
from eightGraph import functions #Import the Function class and the functions dictionary

def main():
    func_list = list(functions.values()) #Get a list of Function objects.
    index = 0

    while True:
        current_function = func_list[index]

        print(f"\nWould you like to see the plot of the following function?")
        print(current_function)  # uses the __str__ method of Function

        user_input = input("Type 'yes' to see the plot, 'next' to skip, or 'exit' to quit: ").strip().lower()

        if user_input == 'yes':
            current_function.plot()
            index = (index + 1) % len(func_list)
        elif user_input == 'next':
            index = (index + 1) % len(func_list)
        elif user_input == 'exit':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()


# import random
# from eightGraph import plot_function, functions
#
# def main():
#     func_names = list(functions.keys())  # Get all function names from eightGraph.py
#     index = 0  # Start with the first function in the list
#
#     while True:
#         # Get the current function name and its details
#         func_name = func_names[index]
#         func_info = functions[func_name]
#
#         # Display the function information
#         print(f"\nWould you like to see the plot of the following function?")
#         print(f"Function: {func_info['label']}")
#         print(f"Description: {func_info['description']}")
#
#         # Ask the user if they want to see this plot
#         user_input = input("Type 'yes' to see the plot, 'next' to skip to the next function, or 'exit' to quit: ").strip().lower()
#
#         if user_input == 'yes':
#             # Display the plot for the current function
#             plot_function(func_name)
#             # After showing the plot, increment index to move to the next function
#             index = (index + 1) % len(func_names)  # Move to the next function
#         elif user_input == 'next':
#             # Skip to the next function without displaying the current plot
#             index = (index + 1) % len(func_names)
#         elif user_input == 'exit':
#             print("Exiting the program. Goodbye!")
#             break
#         else:
#             print("Invalid input. Please type 'yes', 'next', or 'exit'.")
#
# if __name__ == "__main__":
#     main()
