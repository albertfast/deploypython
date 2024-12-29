# Initializing a list
L = [1, 5, 9, 7, 15, 27]
print("Original list:", L, "\n")

# Removing the value 7 from the list
L.remove(7)
print("We removed the value 7 from the list:", L, "\n")

# Deleting the element at index 3 (which is 15)
del(L[3])
print("We deleted the element at index 3 (value 15) from the list:", L, "\n")

# Popping the last element from the list (which is 27)
L.pop()
print("We removed the last element (27) from the list:", L, "\n")

# Working with strings
S = "I<3 cs"
print("Original string:", S, "\n")

# Converting the string to a list of characters
char_list = list(S)
print("Converted string to a list of characters:", char_list, "\n")

# Splitting the string based on the character '<'
result = S.split('<')
print("String split at '<':", result, "\n")

# Joining the string without any separator
joined_string = ''.join(S)
print("Joined the string with no separator:", joined_string, "\n")

# Joining the string with an underscore ('_') between each character
joined_with_underscore = '_'.join(S)
print("Joined the string with an underscore between characters:", joined_with_underscore, "\n")

# Additional list examples for sorting and reversing

# New list for demonstration
L2 = [9, 6, 0, 3, 8, 15, 120, 254, 524, 7]
print("Original L2 list:", L2)

# Using sorted() - this does not mutate the original list
sorted_L2 = sorted(L2)
print("Sorted L2 list using sorted() (does not mutate):", sorted_L2)
print("L2 list after using sorted():", L2, "\n")

# Using sort() - this mutates the original list
L2.sort()
print("L2 list after using sort() (mutates the original list):", L2, "\n")

# Using reverse() - this mutates the original list
L2.reverse()
print("L2 list after using reverse() (mutates the original list):", L2, "\n")

# Combining lists (Concatenation and Extending Lists)
L1 = [2, 1, 3]
L3 = L1 + L2
print("New combined list using + operator:", L3, "\n")  # Combining two lists

L1.extend([0, 6])
print("List L1 after extending with [0, 6]:", L1, "\n")  # Extending the list

# Tuples example
t = (2, "mit", 3)
print("Tuple t:", t)  # Print tuple
print("Element at index 0 in tuple:", t[0])  # Accessing element at index 0

# Tuple içinde liste
t1 = (1, 2, [3, 4])

# Tuple'ın kendisini değiştiremeyiz, bu hata verir:
# t[0] = 5  # Uncommenting this line will give an error

# Ancak tuple içindeki listenin elemanlarını değiştirebiliriz
t1[2][0] = 7
print("Modified tuple:", t1, "\n")  # Output: (1, 2, [7, 4])


# Dictionary example
student = {"name": "Alice", "age": 25, "grade": "A"}
print("Student's name:", student["name"])  # Access value by key
print("Student's age:", student["age"])  # Access value by key
student["major"] = "Computer Science"
print("Updated dictionary:", student)  # Print updated dictionary

for key, value in student.items():
    print(f"Key: {key}, Value: {value}")  # Iterating over dictionary
print(student)

# Dictionary oluşturma
student = {"name": "Alice", "age": 25, "grade": "A"}

# Yeni bir anahtar-değer çifti eklemek
student["major"] = "Computer Science"
print("Updated dictionary:", student, "\n")  # Output: {'name': 'Alice', 'age': 25, 'grade': 'A', 'major': 'Computer Science'}

# Mevcut bir anahtarın değerini değiştirme
student["grade"] = "A+"
print("Updated dictionary:", student, "\n")  # Output: {'name': 'Alice', 'age': 25, 'grade': 'A+', 'major': 'Computer Science'}

# Birden fazla anahtar-değer çifti eklemek
student.update({"hobby": "Reading", "graduation_year": 2023})
print("Dictionary after multiple additions:", student, "\n")  # Output: {'name': 'Alice', 'age': 25, 'grade': 'A+', 'major': 'Computer Science', 'hobby': 'Reading', 'graduation_year': 2023}

# İlk öğrenci bilgileri (dictionary)
student1 = {"name": "Alice", "age": 25, "grade": "A+", "major": "Computer Science"}

# İkinci öğrenci bilgileri (dictionary)
student2 = {"name": "Bob", "age": 22, "grade": "B", "major": "Mathematics"}

# Üçüncü öğrenci bilgileri (dictionary)
student3 = {"name": "Charlie", "age": 23, "grade": "A", "major": "Physics"}

# Tüm öğrencileri tutan ana dictionary (nested dictionary)
students = {
    "student1": student1,
    "student2": student2,
    "student3": student3
}

# Yeni öğrenci eklemek
student4 = {"name": "Diana", "age": 21, "grade": "A-", "major": "Biology"}
students["student4"] = student4

# Ana dictionary'i yazdırmak
print("All students:", students, "\n")

# Belirli bir öğrencinin bilgilerini almak (örneğin, student2)
print("Student2 info:", students["student2"], "\n")

# Yeni öğrenci bilgilerini güncelleme
students["student1"]["age"] = 26
print("Updated student1 info:", students["student1"])

# Aliases: Creating an alias for the same list
warm = ['red', 'yellow', 'orange']
hot = warm  # hot is an alias for warm

# Modifying hot will affect warm since they refer to the same list object
hot.append('pink')

# Output both hot and warm to show that modifying hot affects warm
print("hot list:", hot)   # hot list: ['red', 'yellow', 'orange', 'pink']
print("warm list:", warm) # warm list: ['red', 'yellow', 'orange', 'pink']

# Cloning a list: Copying cool list to chill (they are now separate lists)
cool = ['blue', 'green', 'grey']
chill = cool[:]  # This creates a new list that is a copy of 'cool'

# Modifying chill won't affect cool
chill.append('black')
print("cool list:", cool)   # cool list: ['blue', 'green', 'grey']
print("chill list:", chill) # chill list: ['blue', 'green', 'grey', 'black']

# Sorting Lists:
# Using sort() to mutate the list
warm.sort()
print("warm list after sort():", warm)  # warm list after sort(): ['orange', 'pink', 'red', 'yellow']

# Using sorted() to return a new sorted list without mutating the original list
sorted_cool = sorted(cool)
print("sorted_cool (using sorted()):", sorted_cool)  # sorted_cool: ['blue', 'green', 'grey']
print("cool list after sorted():", cool)             # cool list is unchanged: ['blue', 'green', 'grey']

# Nested Lists: Creating a list of lists
brightcolors = [warm, hot]
print("brightcolors list (before changes):", brightcolors)  # brightcolors list: [['orange', 'pink', 'red', 'yellow'], ['orange', 'pink', 'red', 'yellow']]

# Modifying one of the inner lists
hot.append('purple')
print("hot list after append:", hot)                       # hot list: ['orange', 'pink', 'red', 'yellow', 'purple']
print("brightcolors list (after hot changes):", brightcolors)  # brightcolors reflects the changes in hot: [['orange', 'pink', 'red', 'yellow', 'purple'], ['orange', 'pink', 'red', 'yellow', 'purple']]


# Define two strings
x = "Mother's Day May 12th"
y = "Father's Day June 16th"

# Split both strings into lists of words
x = x.split()
y = y.split()

# Global z: created as an empty list and filled later
z = [x[i] if not j else y[i] for i in range(len(x)) for j in range(2)]

# Print the global z
print("Global z before function call:", z)

# Define a function with its own local z
def simple_func():
    # Local z inside the function
    z = [f"{x[i]}-{y[i]}" for i in range(len(x))]
    print("Local z inside the function:", z)
    return z

# Call the function
local_z = simple_func()

# Print the global z after function call
print("Global z after function call:", z)

# Print the returned local z from the function
print("Returned local z:", local_z)

# Print global z joined as a string
print("Global z joined:", " ".join(z))

