import math

class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

# ===========================================
# Example: Division Function with Exceptions
# ===========================================
def divide_numbers(a, b):
    """
    Divides two numbers with detailed exception handling.

    Parameters:
    - a: Dividend (numerator).
    - b: Divisor (denominator).

    Returns:
    - The division result or None if an exception occurs.
    """
    try:
        result = a / b
        # Successful division
        return result
    except ZeroDivisionError as e:
        # Catches division by zero error
        print(f"Error: Division by zero is not allowed. ({e})")
        return None
    except TypeError as e:
        # Catches invalid type error (e.g., passing a string instead of a number)
        print(f"Error: Both inputs must be numbers. ({e})")
        return None
    finally:
        # Code here runs regardless of whether an exception occurred or not
        print(f"Executed division of {a} by {b}.\n")


# ===========================================
# Example: Accessing Dictionary Values Safely
# ===========================================
def get_dict_value(dictionary, key):
    """
    Safely retrieves a value from a dictionary.

    Parameters:
    - dictionary: The dictionary to retrieve from.
    - key: The key whose value needs to be retrieved.

    Returns:
    - The value for the given key or None if an exception occurs.
    """
    try:
        value = dictionary[key]
        # Key exists in the dictionary
        return value
    except KeyError as e:
        # Catches key not found error
        print(f"Error: The key '{key}' does not exist in the dictionary. ({e})")
        return None
    except TypeError as e:
        # Catches invalid key type (e.g., passing an unhashable type like a list)
        print(f"Error: The dictionary key must be a valid hashable type. ({e})")
        return None
    finally:
        # Executed after key lookup attempt
        print(f"Attempted to access key '{key}' in the dictionary.\n")


# ===========================================
# Example: File Reading with Exception Handling
# ===========================================
def read_file(file_path):
    """
    Tries to read a file and handles common errors like file not found.

    Parameters:
    - file_path: The path to the file to be read.

    Returns:
    - The content of the file as a string or None if an exception occurs.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content read successfully.")
            return content
    except FileNotFoundError as e:
        # Catches file not found error
        print(f"Error: The file '{file_path}' does not exist. ({e})")
        return None
    except IOError as e:
        # Catches general I/O errors
        print(f"Error: An I/O error occurred. ({e})")
        return None
    finally:
        # Always runs, useful for cleanup or logging
        print(f"Attempted to read file '{file_path}'.\n")


# ===========================================
# Example: Custom Exception for Invalid Input
# ===========================================
def calculate_square_root(number):
    """
    Demonstrates raising a custom exception for invalid input.

    Parameters:
    - number: The number whose square root is to be calculated.

    Returns:
    - The square root if the input is valid.
    """
    try:
        if number < 0:
            raise NegativeNumberError("Cannot calculate the square root of a negative number.")
        # Successful calculation
        return math.sqrt(number)
    except NegativeNumberError as e:
        # Catches the custom exception
        print(f"Custom Error: {e}")
        return None
    finally:
        # Always executed
        print(f"Attempted to calculate the square root of {number}.\n")


input_list_1 = ['Hello', ' from', 123, 456, ' AskPython']
input_list_2 = [123, 456, ' AskPython']

def add_list(ip):
    # Adds all items of a list
    # Will raise ValueError if any integer item > 200
    # and will raise TypeError if addition operands are of different types
    if isinstance(ip, list):
        result = '' if isinstance(ip[0], str) else 0
        for item in ip:
            if isinstance(item, int) and item > 200:
                raise ValueError('Integer Item has to be <= 200')
            result = result + item
        return result
    else:
        return None
try:
    # Will raise TypeError
    res = add_list(input_list_1)
    print(res)
except TypeError as te:
    print(type(te), te)
except ValueError as ve:
    print(type(ve), ve)

try:
    # Will raise ValueError since 456 > 200
    res = add_list(input_list_2)
    print(res)
except TypeError as te:
    print(type(te), te)
except ValueError as ve:
    print(type(ve), ve)

# ===========================================
# Main Program for Demonstrations
# ===========================================
def main():
    # Demonstrating division
    print("Division Examples:")
    print("10 / 2:", divide_numbers(10, 2))  # Normal division, should return 5.0
    print("10 / 0:", divide_numbers(10, 0))  # ZeroDivisionError example
    print("10 / 'a':", divide_numbers(10, 'a'))  # TypeError example

    # Demonstrating dictionary key access
    sample_dict = {"name": "Alice", "age": 30}
    print("\nDictionary Access Examples:")
    print("Access 'name':", get_dict_value(sample_dict, "name"))  # Normal case, should return 'Alice'
    print("Access 'salary':", get_dict_value(sample_dict, "salary"))  # KeyError example
    print("Access 123:", get_dict_value(sample_dict, 123))  # KeyError example

    # File operation
    print("\nFile Reading Examples:")
    print(read_file("sample.txt"))  # FileNotFoundError example

    # Custom exception handling
    print("\nCustom Exception Example:")
    print("Square root of 16:", calculate_square_root(16))  # Should return 4.0
    print("Square root of -16:", calculate_square_root(-16))  # Custom NegativeNumberError example

    # Adding list operations and handling exceptions
    print("\nList Addition Examples:")
    input_list_1 = [1, 2, "3", 4]  # This will trigger TypeError
    input_list_2 = [50, 100, 456]  # This will trigger ValueError because 456 > 200

    try:
        print("Processing input_list_1:", input_list_1)
        res = add_list(input_list_1)
        print("Result:", res)
    except TypeError as te:
        print("Caught TypeError for input_list_1:", type(te), te)
    except ValueError as ve:
        print("Caught ValueError for input_list_1:", type(ve), ve)

    try:
        print("\nProcessing input_list_2:", input_list_2)
        res = add_list(input_list_2)
        print("Result:", res)
    except TypeError as te:
        print("Caught TypeError for input_list_2:", type(te), te)
    except ValueError as ve:
        print("Caught ValueError for input_list_2:", type(ve), ve)


if __name__ == "__main__":
    main()
