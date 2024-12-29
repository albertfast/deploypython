def slicingStringListAndTuple(input_str, input_list, input_tuple):
    """
    This function performs several slicing tasks on the given string, list, and tuple.
    It slices parts of the input, prints reversed values, and uses negative indexing to slice from the end.
    """

    # Task 2: Print the substring 'Slice' from the input string
    # Here we slice from index 7 to 11 to get 'Slic' and then append the character 'e' to complete the word 'Slice'.
    print(input_str[7:11] + 'e')  # Output: 'Slice'

    # Task 4: Prompt user for input and slice string, list, and tuple based on the input
    # We ask the user how many characters they want to extract from the beginning of the string, list, and tuple.
    num_chars = int(input("How many characters would you like to extract: "))

    # Slice the first 'num_chars' characters from the string
    # We extract the first 'num_chars' characters of the string and print them.
    print(input_str[:num_chars])  # Outputs the first 'num_chars' characters of the string

    # Slice the first 'num_chars' elements from the list
    # We extract the first 'num_chars' elements from the list and print them.
    print(input_list[:num_chars])  # Outputs the first 'num_chars' elements of the list

    # Slice the first 'num_chars' elements from the tuple
    # We extract the first 'num_chars' elements from the tuple and print them.
    print(input_tuple[:num_chars])  # Outputs the first 'num_chars' elements of the tuple

    # Task 5: Use negative indexing to dynamically slice the last 'num_chars' elements of string, list, and tuple
    # Negative indexing starts from the end of the string/list/tuple. Here, we dynamically slice and print the last 'num_chars' characters/elements.

    # Slice the last 'num_chars' characters from the string using negative indexing
    # Negative slicing starts from the end, so this extracts the last 'num_chars' characters of the string.
    print(input_str[-num_chars:])  # Outputs the last 'num_chars' characters of the string

    # Slice the last 'num_chars' elements from the list using negative indexing
    # Similarly, this extracts the last 'num_chars' elements of the list.
    print(input_list[-num_chars:])  # Outputs the last 'num_chars' elements of the list

    # Slice the last 'num_chars' elements from the tuple using negative indexing
    # Lastly, this extracts the last 'num_chars' elements of the tuple.
    print(input_tuple[-num_chars:])  # Outputs the last 'num_chars' elements of the tuple

    # Task 6: Print the string, list, and tuple in reverse order using negative step slicing
    # The [::-1] slicing notation means we step backwards through the entire string/list/tuple, effectively reversing it.

    # Reverse the string
    print(input_str[::-1])  # This prints the string in reverse order.

    # Reverse the list
    print(input_list[::-1])  # This prints the list in reverse order.

    # Reverse the tuple
    print(input_tuple[::-1])  # This prints the tuple in reverse order.


# Main program logic
if __name__ == "__main__":
    """
    This is the main part of the program where the predefined values for the string, list, and tuple are set.
    We then call the function slicingStringListAndTuple to perform the slicing tasks on the input data.
    """

    # Assigning a string to the variable 'str_data'
    # This string will be used for slicing tasks in the function.
    str_data = "Python Slicing"

    # Creating a list of characters from the string 'Python Slicing'
    # We use a list comprehension to extract each character from the string except spaces.
    # l = [char for char in str_data if char != ' ']  # List of characters from the string, excluding spaces
    l = ['P', 'y', 't', 'h', 'o', 'n', 'S', 'l', 'i', 'c', 'i', 'n', 'g']

    # Creating a tuple of characters from the string 'Python Slicing'
    # We convert the list 'l' into a tuple to use in the slicing tasks.
    # t = tuple(l)  # Tuple created from the list 'l'
    t = ('P', 'y', 't', 'h', 'o', 'n', 'S', 'l', 'i', 'c', 'i', 'n', 'g')

    # Calling the function with predefined values
    # We pass the string, list, and tuple to the function slicingStringListAndTuple to perform various slicing tasks.
    slicingStringListAndTuple(str_data, l, t)



'''
def slicingStringListAndTuple(input_str, input_list, input_tuple):
    # Task 2: Print the substring 'Slice' from the input string
    print(input_str[7:11] + 'e')  # Output: Slice

    # Task 4: Prompt user for input and slice string, list, and tuple based on the input
    num_chars = int(input("How many characters would you like to extract: "))

    # İlk 'num_chars' karakteri dilimle ve yazdır
    print(input_str[:num_chars])  # String'in ilk 'num_chars' karakteri
    print(input_list[:num_chars])  # Listenin ilk 'num_chars' elemanı
    print(input_tuple[:num_chars])  # Tuple'ın ilk 'num_chars' elemanı

    # Task 5: Use negative indexing to dynamically slice the last 'num_chars' elements of string, list, and tuple
    print(input_str[-num_chars:])  # String'in son 'num_chars' karakteri
    print(input_list[-num_chars:])  # Listenin son 'num_chars' elemanı
    print(input_tuple[-num_chars:])  # Tuple'ın son 'num_chars' elemanı

    # Task 6: Print the string, list, and tuple in reverse order using negative step slicing
    print(input_str[::-1])  # Reverses the string 'str'
    print(input_list[::-1])  # Reverses the list 'l'
    print(input_tuple[::-1])  # Reverses the tuple 't'


# Main program logic
if __name__ == "__main__":
    # Assigning a string to the variable 'str'
    str_data = "Python Slicing"

    # Creating a list of characters from the string 'Python Slicing'
    l = [char for char in str_data if char != ' ']

    # Creating a tuple of characters from the string 'Python Slicing'
    t = tuple(l)

    # Calling the function with predefined values
    slicingStringListAndTuple(str_data, l, t)
'''
'''
# Assigning a string to the variable 'str'
str = "Python Slicing"

# Creating a list of characters from the string 'Python Slicing'
l = [char for char in str if char != ' ']

# Creating a tuple of characters from the string 'Python Slicing'
t=tuple(l)

# Task 3: Extract specific elements to form the word "Sing" from the list 'l' and store in 'song'
# Slicing the list 'l' from index 6 to 13, skipping every 4th element to get 'S' and 'i'
# then appending characters 'n' and 'g' from index 11 to 13
song = l[6:13:4] + l[11:13] 
# Verifying the slicing result by printing ==>  
print("song: ", song) ==> Expected output: ['S', 'i', 'n', 'g']

# Task 3: Extract elements to form the tuple ('o', 'n') from the tuple 't' and store in 'notOff'
# Slicing the tuple 't' from index 4 to 6 to get 'o' and 'n'
notOff = t[4:6]  
# Verifying the slicing result by printing ==> 
print("notOff: ", notOff) ==>  # Expected output: ('o', 'n')

# Task 2: Print the substring 'Slice' from 'str'
# Slicing 'str' from index 7 to 11 to extract 'Slic' and appending 'e' to form 'Slice'
print(str[7:11] + 'e')  # Output: Slice

# Task 4: Prompt user for input and slice string, list, and tuple based on the input
# Asking the user for the number of characters to extract
num_chars = int(input("How many characters would you like to extract: "))
# Slicing 'str', 'l', and 't' up to the number input by the user and printing the results
print(str[:num_chars])  # Outputs the first 'num_chars' characters of 'str'
print(l[:num_chars])    # Outputs the first 'num_chars' elements of 'l'
print(t[:num_chars])    # Outputs the first 'num_chars' elements of 't'

# Task 5: Use negative indexing to slice the last 3 elements of string, list, and tuple
# Printing the last three characters/elements using negative indexing
print(str[-3:])  # Outputs the last 3 characters of 'str'
print(l[-3:])    # Outputs the last 3 elements of 'l'
print(t[-3:])    # Outputs the last 3 elements of 't'

# Task 6: Print the string, list, and tuple in reverse order using negative step slicing
# Reversing and printing 'str', 'l', and 't' using a step of -1
print(str[::-1])  # Reverses the string 'str'
print(l[::-1])    # Reverses the list 'l'
print(t[::-1])    # Reverses the tuple 't'
'''

'''
# Assigning a string to the variable 'str'
str = "Python Slicing"
num_chars2 = 14
#l = [char for char in str if char != ' ']
l = (str[:num_chars2])
print('l = ',l)
t=tuple(l)

print(str[:num_chars2])
print(l[:num_chars2])
print(t[:num_chars2])
song = l[6:7] + l[8:13:3] + l[12:13]
kong= l[6:10:2] + l[11:13]
cong= l[6:13:4] + l[11:13]
print("song: ", song)
print("kong: ", kong)
print("cong: ", cong)
notOff = t[4:6]
print("notOff: ", notOff)

num_chars = int(input("How many characters would you like to extract: "))
print(str[:num_chars])
print(l[:num_chars])
'''








'''
t = str[0],str[1],str[2],str[3],str[4],str[5],str[7],str[8],str[9],str[10],str[11],str[12],str[13]
l = list(t)

str = "Ahmet Hasim Sahiner"
l = [char for char in str if char != ' ']
print('l = ',l)
t=tuple(l)
print('t = ',t)


'''

'''
# Function to square a number
def square(x):
    y = x * x # Multiply x by itself
    print(f"square({x}) = {y} (This is {x} multiplied by itself)")
    return y

# Function to calculate the sum of squares of three numbers with additional steps
def sum_of_squares(x, y, z):
    a = square(x)  # Calculate square of the first number
    print(f"Step 1: First square calculated, a = {a} (This is the square of {x})")

    # Add the square of z to a (instead of x) for variety
    a += square(z)  # Recalculate square of z and add it to 'a'
    print(f"Step 2: Added square(z), new a = {a} (The square of {z} was added to a)")

    b = square(y)  # Calculate square of the second number
    print(f"Step 3: Second square calculated, b = {b} (This is the square of {y})")

    # Add the square of b to itself
    b += square(b)  # Recalculate square of b and add it to itself
    print(f"Step 4: Added square(b) to b, new b = {b} (The square of {b} was added to itself)")

    c = square(z)  # Calculate square of the third number
    print(f"Step 5: Third square calculated, c = {c} (This is the square of {z})")

    # Add the square of a to c
    c += square(a)  # Add square of a to c
    print(f"Step 6: Added square(a) to c, new c = {c} (The square of a was added to c)")

    # Print the individual squared values and their sum
    print(f"sum_of_squares({x}, {y}, {z}) = {a} + {b} + {c} = {a + b + c} (Adding all the squares together)")
    return a + b + c

# Values to square
a = -5
b = 2
c = 10

# Print initial values
print(f"Initial values: a = {a}, b = {b}, c = {c}")

# Calculate the sum of squares
result = sum_of_squares(a, b, c)

# Print the final result
print(f"Final result: {result} (The sum of squares of {a}, {b}, and {c})")
'''

