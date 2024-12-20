        #                             r
        #                             r
        #                             Abrak
        #                             Abrakadab
        # Abrakadabra
        #                             Arkdba
        #                             baaar
        #                             arbadakarbA
        #                             abdkrA
        #                             11

str_input = input("Enter the string: ")
# Count the number of spaces in the input string
num_spaces = str_input.count(' ')
# The number of words is the number of spaces + 1
num_words = num_spaces + 1 # print(num_words)
first_occurrence = str_input.find('f')
last_occurrence = str_input.rfind('f')

# 1. Third character of the string
print(str_input[2])

# 2. Second to last character of the string
print(str_input[-2])

# 3. First five characters of the string
print(str_input[:5])

# 4. All but the last two characters
print(str_input[:-2])

# 5. Characters with even indices
print(str_input[::2])

# 6. Characters with odd indices
print(str_input[1::2])

# 7. All characters in reverse order
print(str_input[::-1])

# 8. Every second character in reverse order, starting from the last one
print(str_input[::-2])

# 9. Length of the string
print(len(str_input))

print(num_words)

if first_occurrence == -1:
    print(-1)
elif first_occurrence == last_occurrence:
    print(first_occurrence)
else:
    print(first_occurrence, last_occurrence)


