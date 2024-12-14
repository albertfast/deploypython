def sliceAndRevList(input_list):
    """
    This function processes a list in two steps:
    1. It extracts the first, third, and fifth items from the input list using a loop.
    2. It reverses the extracted items and returns them as a new list.

    Here's how it works:
    - The function iterates over the input list, checking specific indices (0, 2, and 4).
    - It adds those items to a temporary list.
    - Then it reverses the temporary list and returns it.
    """

    # Step 1: Create an empty list to store the first, third, and fifth items
    second_list = []

    # Iterate over the indices of the input list
    for i in range(len(input_list)):
        # Check if the index is one of the desired ones (0, 2, or 4)
        if i in [0, 2, 4]:
            second_list.append(input_list[i])  # Add the item at that index to second_list

    # Step 2: Reverse the second_list to create the final output
    third_list = []
    for item in reversed(second_list):  # Iterate over second_list in reverse order
        third_list.append(item)  # Add each reversed item to third_list

    # Return the final processed list
    return third_list


# Example usage
original_list = [55, 18, 32, 24, 99, 88]  # The original list to process
result = sliceAndRevList(original_list)  # Call the function and store the result

# Output the results
print(f"Original list: {original_list}")
print(f"Processed list: {result}")