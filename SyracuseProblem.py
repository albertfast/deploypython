from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Step 2: Initialize the result list with the first interval
        merged = [intervals[0]]

        # Step 3: Iterate through the intervals
        for current in intervals[1:]:
            # Get the last interval in the merged list
            previous = merged[-1]

            # Step 4: Check if current interval overlaps with the previous interval
            if current[0] <= previous[1]:  # Overlapping
                # Merge the intervals
                previous[1] = max(previous[1], current[1])
            else:
                # If no overlap, add the current interval to the result
                merged.append(current)

        # Step 5: Return the merged intervals
        return merged

# Main program to accept user input
if __name__ == "__main__":
    solution = Solution()  # Create an instance of the Solution class

    # Step 1: Ask the user for the number of intervals
    print("Enter the number of intervals:")
    n = int(input())  # Number of intervals

    # Step 2: Initialize an empty list to store the intervals
    intervals = []

    # Step 3: Collect the intervals from the user
    print("Enter the intervals (start and end values separated by space):")
    for _ in range(n):
        interval = list(map(int, input().split()))  # Read and convert each interval to a list of integers
        intervals.append(interval)

    # Step 4: Call the merge method and print the result
    print("Merged intervals:")
    print(solution.merge(intervals))