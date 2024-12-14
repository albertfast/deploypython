x = {"Toyota": "yaris", "Bmw": "3.30",  "Mercedes": "C63"}
del x["Toyota"]    # You can access the value by entering its key
print(x)
# You can create an empty dictionary with either an empty dict() or the empty braces {}
# y = {}
####################################
x = {
  "a": {
    "b": [
       {"c": "Hello!"}
     ]
  }
}
print(x)
print(x.get("a").get("b"))
print(x["a"]["b"][0]["c"])

#########################################3

text = """NARRATOR: A year passed. Winter changed into Spring. Spring changed
into Summer. Summer changed back into Winter. And Winter gave Spring
and Summer a miss and went straight on into Autumn. Until one day..."""
text = text.replace(".", "").replace(":", "")
text = text.split()
text = [w.lower() for w in text]
print(text)

freq = {}
for word in text:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(freq)

##############################3

# Center of a cluster:
# Given a dictionary of points and their weight, find the weighted center.
points = {
    (0, 0): 1,
    (1, 0): 7,
    (0, 1): 10,
    (-1, 0): 28,
    (0, -1): 35
}

tot_x = 0
tot_y = 0
for k in points.keys():
    tot_x += k[0] * points[k]
    tot_y += k[1] * points[k]

weight_sum = - sum(points.values())
avg_x = tot_x / weight_sum
avg_y = tot_y / weight_sum
print("Avg X =", avg_x, "Avg Y =", avg_y)

##############################################3

# 1. Yöntem
dict1 = {'A': 1, 'B': 2, 'C': 3}

# 2. Yöntem
dict2 = dict(A=1, B=2, C=3)

# 3. Yöntem
dict3 = dict.fromkeys(['X', 'Y', 'Z'], 0)

# 4. Yöntem
LOT = [("X", 0), ("Y", 0), ("Z", 0)]
dict4 = dict(LOT)

# 5. Yöntem
L1 = ["X", "Y", "Z"]
L2 = [0, 0, 0]
dict5 = dict(zip(L1, L2))

# dict6 = {A: 1, B: 2, C: 3 } WRONG!

# Sözlükleri bir listeye koyma
dicts = [dict1, dict2, dict3, dict4, dict5]

# For döngüsü ile sırayla yazdırma
for i, d in enumerate(dicts, start=1):
    print(f"Dictionary {i}: {d}")

###############################################

cart = { 'fruit': 3, 'dairy': 0 , 'veggie': 4} # Use the 'in' keyword

if 'veggie' in cart:
    cart['veggie'] = cart['veggie'] + 1
else:
    cart['veggie'] = 1

print(cart) # {'fruit': 3, 'dairy': 0, 'veggie': 5}

cart1 = { 'fruit': 4, 'dairy': 0 , 'veggie': ['banana', 'apple', 'orange', 'mango']}
print(f"We have {cart1['fruit']} fruits in our cart {cart1['veggie']}")

del cart1['fruit']
cart1.pop('dairy')
print(len(cart1))
print(cart1)

#############################################

# Dictionary representing program completion status
# Keys are course codes, values are 1 (completed) or 0 (not completed)
program = {
    '101': 1,
    '102': 1,
    '201': 1,
    '202': 1,
    '301': 0,
    '302': 0,
    '401': 0
}

# Variables to track the last completed course and the first incomplete course
last_completed_course = None
first_incomplete_course = None

# Iterate through the dictionary
for course, status in program.items():
    if status == 1:  # If the course is completed
        last_completed_course = course  # Update the last completed course
    elif status == 0 and first_incomplete_course is None:  # If the course is not completed and it's the first one
        first_incomplete_course = course  # Set the first incomplete course

# Print the results
if last_completed_course:
    print(last_completed_course + " is complete!")

if first_incomplete_course:
    print(first_incomplete_course + " is almost complete!")
###############################

# Access keys, values, and key-value pairs
keys = program.keys()  # dict_keys(['101', '102', '201', '202', '301', '302', '401'])
values = program.values()  # dict_values([1, 1, 1, 0, 0, 0, 0])
key_and_values = program.items()  # dict_items([('101', 1), ('102', 1), ..., ('401', 0)])

# Iterate over keys
for k in keys:
    print(f"Key: {k}")

# Iterate over values
for v in values:
    print(f"Value: {v}")

# Iterate over key-value pairs
for kv in key_and_values:
    print(f"Key-Value Pair: {kv}")

dict9 = {'X': 0, 'Y': 0, 'Z': 0}
dict9['A'] = 2
dict9['X'] = 9
print(dict9) # {'X': 9, 'Y': 0, 'Z': 0, 'A': 2}











































































