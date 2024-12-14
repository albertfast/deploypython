def sortedList(nums):
    # Time Complexity: O(n) -> This function assumes the list is already sorted.
    # The loop iterates through the list with a step of 2, making a linear traversal.
    # Since each element is visited once, the complexity is O(n).

    # Space Complexity: O(1) -> No extra data structures are used. The function operates in constant space.

    for i in range(0, len(nums) - 1, 2): #Listenin ilk(0) elemanindan baslayip sondan bitrinci(-1) elemanina kadar 2 ser 2 ser gider
        if nums[i] != nums[i + 1]:  # If the current element is not equal to the next one
            return nums[i] # Return the element that does not have a pair
    return nums[-1]  # Return the last element if no other single element is found
nums = [1,1,3,3,5]
print("Sorted List Different number = ",sortedList(nums))

def unsortedList(nums):
    nums.sort() # duzensiz bir listeyi kucukten buyuge siralar
    # Time Complexity: O(n log n) -> Sorting the array takes O(n log n), and iterating through the sorted array is O(n).
    # Space Complexity: O(1) -> Sorting is done in-place, so no additional space is required.
    for i in range(0, len(nums) - 1, 2): #Listenin ilk(0) elemanindan baslayip sondan bitrinci(-1) elemanina kadar 2 ser 2 ser gider
        if nums[i] != nums[i + 1]:
            return nums[i]
    return nums[-1]

nums = [5, 8, 7, 10, -10, 5, 7, -10, 8]
print("Different number = ",unsortedList(nums))


def single_number_in_unsorted_maxn(nums):
    # Time Complexity: O(n) -> Looping through the list to increment counts is O(n),
    # and looping through the count array to find the single number is also O(n).
    # Overall time complexity is O(n).

    # Space Complexity: O(n) -> The counting array has a size of n+1, so it requires O(n) space.

    # Create a counting array initialized to 0
    count = [0] * (len(nums) + 1)

    # Increment count for each number
    for num in nums:
        count[num] += 1

    # Find the number that appears exactly once
    for i in range(len(count)):
        if count[i] == 1:
            return i


nums = [4, 1, 2, 1, 2, 4, 6, 8, 5, 8, 5]
print(single_number_in_unsorted_maxn(nums))


def singleNumber2(nums):
    # Time Complexity: O(n) -> A single pass through the list is O(n).
    # Space Complexity: O(1) -> No additional data structures are used; constant space is required.

    result = 0
    for num in nums:
        result ^= num  # XOR all numbers
    return result

nums = [4, 1, 2, 1, 2, 4, 6, 6, 5, 8, 5]
print(singleNumber2(nums))
