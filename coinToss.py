import random  # Import the random module to generate random numbers
from functools import reduce  # Import reduce for accumulating results

# Step 1: Ask the user to input how many coin tosses to perform
num_tosses = int(input("Enter the number of tosses to perform: "))

# Step 2: Generate a list of coin toss results using list comprehension and random.randint()
# Each result will be either 0 (representing Heads) or 1 (representing Tails)
results = [random.randint(0, 1) for _ in range(num_tosses)]

# Step 3: Use the reduce function to count the number of times "Heads" (0) appears in the results
# The lambda function checks each value in the list and adds 1 to the accumulator if the value is 0 (Heads)
count_heads = reduce(lambda acc, val: acc + (1 if val == 0 else 0), results, 0)

# Step 4: Calculate the number of tails by subtracting the number of heads from the total number of tosses
count_tails = num_tosses - count_heads  # The remaining results will be Tails

# Additional loop to display each toss result for visualization purposes
counter = 0  # Initialize the counter to keep track of the number of iterations

# Step 5: Start a loop that runs until the counter reaches the number of tosses
while counter < num_tosses:
    # Step 6: Generate a random number (0 or 1) for each toss
    result = random.randint(0, 1)

    # Step 7: Check if the result is 0, which represents "Heads"
    if result == 0:
        print("Heads")  # Print "Heads" if the result is 0
    else:
        print("Tails")  # Print "Tails" if the result is 1

    # Step 8: Increment the counter by 1 to move to the next iteration
    counter += 1
