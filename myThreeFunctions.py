# File: myThreeFunctions.py

# Import necessary functions and variables from slicingStringListAndTuple
# I'm importing the slicingStringListAndTuple function, str_data (a string), l (a list), and t (a tuple) 
# from slicingStringListAndTuple.py.
from slicingStringListAndTuple import slicingStringListAndTuple, str_data, l, t


def myAvgfun(a, b, c, d, e):
    """
    This function calculates the average of five numbers.
    
    Parameters:
    - a, b, c, d, e: The five numbers to calculate the average.
    
    Returns:
    - The average of the five numbers.
    
    From what I understand, this function takes the five numbers, adds them up, and divides by 5 to calculate the average.
    In Python, division always returns a float (decimal number), so the expected output will be a float.
    """
    return (a + b + c + d + e) / 5  # Add the five numbers and divide by 5 to find the average.


def myOwnFunction():
    """
    This is my custom function that prints a message.
    
    This function doesn't take any parameters and simply prints a predefined message.
    The goal here is to demonstrate a simple function that outputs something to the console.
    """
    print("My function just prints this sentence.")


# Main program logic
if __name__ == "__main__":

    # Step 1: Call the myAvgfun function with the numbers 1, 2, 3, 4, and 5 to calculate their average
    # Logic: These numbers will be passed to myAvgfun to calculate the average.
    avg = myAvgfun(1, 2, 3, 4, 5)

    # Step 2: Print the result of the average calculation.
    # On the console, I expect to see "Average: 3".
    print("Average:", avg)  # The average of 1, 2, 3, 4, and 5 should be 3.

    # Adding a blank line for better readability in the console output.
    print("\n")

    # Step 3: Call the slicingStringListAndTuple function with str_data, l, and t.
    # Logic: This function will perform various slicing operations on the string, list, and tuple.
    slicing_results = slicingStringListAndTuple(str_data, l, t)

    # Step 4: Iterate through the results of the slicing operations and print each result.
    # Logic: slicingStringListAndTuple returns a list of results, and here I am printing each one.
    for result in slicing_results:
        print(result)  # Each slicing result is printed to the console.

    # Adding another blank line to make the output more readable.
    print("\n")

    # Step 5: Call myOwnFunction.
    # Logic: This function just prints a simple message ("My function just prints this sentence.") to the console.
    myOwnFunction()  # This prints a simple message to the console.
