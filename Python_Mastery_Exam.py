# def binary_search_steps(arr, target):
#     steps = []  # To store the elements visited during the search
#     left, right = 0, len(arr) - 1  # Define the search boundaries
#
#     while left <= right:
#         # Calculate the middle index; choose the smaller middle if the length is even
#         mid = left + (right - left) // 2
#
#         steps.append(arr[mid])  # Record the current middle element
#
#         if arr[mid] == target:
#             return steps  # Target found, return the steps
#         elif arr[mid] < target:
#             left = mid + 1  # Narrow search to the right half
#         else:
#             right = mid - 1  # Narrow search to the left half
#
#     return steps  # If the target is not found, return the steps visited
#
# # Example usage:
# arr = [12, 18, 24, 37, 42, 53, 64, 71, 76, 80, 85, 92, 100]
# target = 85
# steps = binary_search_steps(arr, target)
# print("Steps taken during the search:", steps)


# Verilen sözlük
hmap = {
    "cart": {
        "fruit": [("apple", 1), ("banana", 2), ("orange", 3)],
        "vegetable": [("carrot", 1), ("cucumber", 2), ("lettuce", 3)]
    },
    "total": 12
}

# "cucumber" elemanına erişim
x = hmap["cart"]["vegetable"][0][0]

# Sonucu yazdır
print(x)  # Beklenen çıktı: cucumber




