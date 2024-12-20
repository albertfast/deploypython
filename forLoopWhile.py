a = ["apple", "banana", "cherry"]
for element in a:
    print(f"{element}", end=" ")
print("")

b = [20, 10, 5]
total = 0
for e in b:
    total += e
    print(f"{e}", end=" ")
print("")
print(f"Total = {total}", end=" ")
print("")


d = list(range(1,7))
print(d) #[1, 2, 3, 4, 5, 6]

print(list(range(1,7))) #[1, 2, 3, 4, 5, 6]

for i in range(1, 7):
    print(f"{i}", end=" ") # 1 2 3 4 5 6
print("")

total2 = 0
for i in range(1, 10): # 1 2 3 4 5 6 7 8 9
    print(f"{i}", end=" ")
    if i % 3 == 0:   # 3 + 6 + 9 = 18
        total2 += i
print("")
print(f"total of = {total2}")

total3 = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 ==0:
        print(f"{i}+", end="")
        total3 += i
print(f"= {total3}")

# initializes all the 10 spaces with 0’s
a = [0] * 10
print("Intitialising empty list with zeros: ", a)

# initializes all the 10 spaces with None
b = [None] * 10
print("Intitialising empty list of None: ", b)

# initializes a 4 by 3 array matrix all with 0's
c =  [[0] * 3] * 2
print("Intitialising 2D empty list of zeros: ", c)

# empty list which is not null, it's just empty.
d = []
print("Intitialising empty list of zeros: ", d)

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
    # Create a counting array initialized to 0
    count = [0] * (len(nums) + 1)
# time complexity of O(n),  space complexity  of o(1)
    # Increment count for each number
    for num in nums:
        count[num] += 1

    # Find the number that appears exactly once
    for i in range(len(count)):
        if count[i] == 1:
            return i
nums = [4,1,2,1,2,4,6,6,5,8,5]
print(single_number_in_unsorted_maxn(nums))


def singleNumber2(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR all numbers
    return result
nums = [4,1,2,1,2,4,6,6,5,8,5]
print(single_number_in_unsorted_maxn(nums))
