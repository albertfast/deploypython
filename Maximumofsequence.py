#Given a sequence of non-negative integers, where each number is written (input) in a separate line. The sequence ends with 0.
# Print the maximum of the sequence.

maximum_number = 0
while True:
    input_number = int(input())
    if input_number == 0:
        break
    if input_number > maximum_number:
        maximum_number = input_number
print(maximum_number)