# File: slicingStringListAndTuple.py

# Assigning a string to the variable 'str_data'
# This string will be used in various slicing tasks later.
str_data = "Python Slicing"

# Creating a list of characters from the string 'Python Slicing'
# I'm turning the string into a list of individual characters, excluding spaces.
l = ['P', 'y', 't', 'h', 'o', 'n', 'S', 'l', 'i', 'c', 'i', 'n', 'g']

# Creating a tuple of characters from the string 'Python Slicing'
# Similarly, I'm creating a tuple from the same characters, excluding spaces.
t = ('P', 'y', 't', 'h', 'o', 'n', 'S', 'l', 'i', 'c', 'i', 'n', 'g')

def slicingStringListAndTuple(input_str, input_list, input_tuple):
    """
    This function performs several slicing tasks on the given string, list, and tuple.
    It slices parts of the input, prints reversed values, and uses negative indexing to slice from the end.
    Returns a list of results for later printing.

    Here's what I'm doing step by step:
    - Extracting specific parts from the string, list, and tuple.
    - Using slicing and negative indexing to handle different tasks.
    - Returning a list that contains the results of all these slicing operations.
    """

    # I'm creating a list 'results' to store the output of each slicing operation.
    # This will make it easier to print all the results later.
    results = []

    # Task 2: Extract the substring 'Slic' from the string and append 'e' to form 'Slice'
    # I am slicing the string from index 7 to 11 (which extracts 'Slic') and then appending 'e' to form 'Slice'.
    print(input_str[7:11] + 'e')  # Output should be 'Slice'

    # Task 3: Extract specific elements to form the word "Sing" from the list 'l' and store in 'song'.
    # I'm slicing the list to extract the necessary elements ('S', 'i', 'n', 'g').
    song = l[6:13:4] + l[11:13]
    # I'm printing this to verify that I got the expected result.
    print("song = ", song)  # Expected output: ['S', 'i', 'n', 'g']

    # Task 3 (continued): Extract the tuple ('o', 'n') from 't' and store in 'notOff'.
    # I'm slicing the tuple from index 4 to 6 to extract the elements 'o' and 'n'.
    notOff = t[4:6]
    # Printing to verify that the result matches the expected output.
    print("notOff = ", notOff)  # Expected output: ('o', 'n')

    # Task 4: Ask the user how many characters they want to extract.
    # The input is converted to an integer and used for slicing the string, list, and tuple.
    num_chars = int(input("How many characters would you like to extract: "))

    # I'm slicing the first 'num_chars' characters from the string and appending it to the results list.
    results.append(input_str[:num_chars])
    # Same slicing for the list.
    results.append(input_list[:num_chars])
    # Same slicing for the tuple.
    results.append(input_tuple[:num_chars])

    # Task 5: Dynamically slice the last 'num_chars' elements based on user input using negative indexing.
    # Negative indexing means we count from the end of the sequence. For example, [-3:] gives the last 3 elements.
    results.append(input_str[-num_chars:])  # Last 'num_chars' characters from the string.
    results.append(input_list[-num_chars:])  # Last 'num_chars' elements from the list.
    results.append(input_tuple[-num_chars:])  # Last 'num_chars' elements from the tuple.

    # Task 6: Print the string, list, and tuple in reverse order.
    # I'm using the [::-1] slicing method to reverse each of them.
    results.append(input_str[::-1])  # Reversed string.
    results.append(input_list[::-1])  # Reversed list.
    results.append(input_tuple[::-1])  # Reversed tuple.

    # I return the list of results so they can be printed later by the main program.
    return results


# Main program logic
if __name__ == "__main__":
    """
    This block only runs when Program 1 is executed directly. 
    It calls the slicingStringListAndTuple function and handles the results.

    Here's the logic:
    - I call slicingStringListAndTuple with predefined string, list, and tuple values.
    - The results are stored in a list, and I use a loop to print each result one by one.
    """

    # I'm calling the function with the string, list, and tuple that were defined earlier.
    # The function performs all the slicing tasks and returns the results.
    result = slicingStringListAndTuple(str_data, l, t)

    # Using a 'for' loop to print each result in the list 'result'.
    # I do this because all the slicing results are stored in the list and I want to display them.
    for res in result:
        print(res)  # Each result from the slicing function gets printed here.

