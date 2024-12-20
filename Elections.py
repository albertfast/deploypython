# U: Understand the problem
# - Input:
#   1. First line contains an integer n (number of records).
#   2. Each of the next n lines contains a candidate name and their votes.
# - Output:
#   1. Print the total votes each candidate received.
#   2. Candidates should be printed in alphabetical order.

# M: Map out the solution
# - Use a dictionary to store candidate names as keys and their total votes as values.
# - Loop through the input to populate the dictionary.
# - Sort the dictionary keys alphabetically for output.

# P: Plan the steps
# 1. Read the number of records (n).
# 2. Create an empty dictionary to store votes.
# 3. For each record:
#    - Parse the candidate name and votes.
#    - Add votes to the candidate in the dictionary.
# 4. Sort the candidates alphabetically.
# 5. Print the candidate names and their total votes.

# I: Implement the solution

def calculate_votes():
    # Step 1: Read the total number of records
    n = int(input())  # Read the number of records from the first line

    # Step 2: Initialize an empty dictionary to store candidate votes
    vote_counts = {}

    # Step 3: Process each record
    for _ in range(n):
        # Read candidate name and votes from input
        name, votes = input().split()  # Split input into name and votes
        votes = int(votes)  # Convert the votes to an integer

        # If candidate exists in the dictionary, add votes to the current total
        if name in vote_counts:
            vote_counts[name] += votes
        else:
            # If candidate does not exist, initialize with current votes
            vote_counts[name] = votes

    # Step 4: Sort candidates alphabetically by name
    sorted_candidates = sorted(vote_counts.keys())  # Sort the dictionary keys

    # Step 5: Print the sorted results
    for candidate in sorted_candidates:
        print(candidate, vote_counts[candidate])  # Print name and total votes
calculate_votes()

# R: Review the solution
# - Ensure input is processed correctly.
# - Verify the votes are summed accurately.
# - Confirm candidates are sorted alphabetically in the output.

# E: Evaluate and optimize
# - Space complexity: O(n) for storing votes in the dictionary.
# - Time complexity: O(n) for processing votes + O(k log k) for sorting (k: unique candidates).
# - The solution is efficient for the given problem constraints.
