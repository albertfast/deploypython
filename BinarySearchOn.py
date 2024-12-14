term = int(input("Enter a number to search for: "))
def binary_search(term, terms):
    """
    This funciton performs a binary search on a sorted list of numbers.

    Args:
        terms: A sorted list of numbers.
        term: The number to search for in the list.

    Returns:
        The index of the term in the list if found, otherwise -1.
    """
    # Intialize variables for search range boundaries
    low = 0
    high = len(terms) - 1
    mid = 0

    while low <= high:  # Loop continues as search range is valid
        # Calculate middle index of current search range
        mid = (low + high) // 2

        if terms[mid] == term:  # Check if terms is found at middle index
            return mid
        elif terms[mid] < term:  # Eliminate left half if term is greater
            low = mid + 1
        else:  # Eliminate right half if term is less
            high = mid - 1

    return -1  # Term not found if loop completes
print(binary_search(term, [12, 18, 24, 37, 42, 53, 64, 71, 76, 80, 85, 92, 100]))