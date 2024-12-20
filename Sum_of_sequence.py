#Given a sequence of non-negative integers, where each number is written (input) in a separate line.
# The sequence ends with 0.

input_number = int(input())
sum = 0
while input_number != 0:
    sum += input_number
    input_number = int(input())
print(sum)