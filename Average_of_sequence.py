#Given a sequence of non-negative integers, where each number is written (input) in a separate line. The sequence ends with 0. Print the average of the sequence.

input_number = int(input())
average = 0
sequence_count = 0
sum = 0
while input_number !=0:
    sum += input_number
    sequence_count +=1
    average = sum / sequence_count
    input_number = int(input())
print(average)
