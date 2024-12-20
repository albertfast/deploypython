# Understand
# Input: List of Intervals
#         Unsorted
# Output: List of Merged Intervals
# Example: [[1, 8], [7, 15]] -> [[1, 15]]
# Matching or previous problems
# - List and creating list as output
# - Manipulate itself
# - Loops - nested loop - sort
# - Two intervals - merge or not

# Plan
# - 2 inputs
# [[a, b], [c, d]]
# b < c -> no overlap
# c <= b -> Overlap -> [[a, d]]
# c == a -> Overlap -> [[a, d]]
# d < b -> Overlap -> [[a, b]]

# Pseudo code:
# 1. Check if c <= b
#    if d >= b:
#        Update intervals[0][1] = intervals[1][1]
#    Remove the second entry from the intervals

def mergeTwoIntervals(intervals, first_index):
    if(intervals[first_index+1][0] <= intervals[first_index+0][1]):
    # if first_index + 1 < len(intervals):
        if intervals[first_index+1][0] <= intervals[first_index][1]:
            if intervals[first_index+1][1] >= intervals[first_index][1]:
                intervals[first_index][1] = intervals[first_index+1][1]
            intervals.pop(first_index+1)
            return True
    return False

# plan:
# 0: While loop current != len(intervals) - 1
#   1. Check if the current two need to be merged and if yes, merge it
#   2. If the current two merge -> check if the current two again
#   3. If the current two didn’t merge -> check the next two (current +1)
def merge(intervals):
    intervals.sort()
    current = 0
    while True:
        if(current == len(intervals)-1):
            break
        merged = mergeTwoIntervals(intervals, current)
        if (merged == False):
            current = current + 1
    return intervals

print(merge([[1, 4]]))
print(merge([[1, 4], [4, 5]]))
print(merge([[1, 5], [9, 10], [10, 14]]))
print(merge([[1, 5], [8, 10], [13, 15]]))
print(merge([[1, 5], [4, 10], [9, 15], [16, 22], [11,18], [2,8]]))

'''
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
'''

'''
def mergeTwoIntervals(intervals, first_index):
    if(intervals[first_index+1][0] <= intervals[first_index+0][1]):
        if intervals[first_index+1][0] <= intervals[first_index][1]:
            if intervals[first_index+1][1] >= intervals[first_index][1]:
                intervals[first_index][1] = intervals[first_index+1][1]
            intervals.pop(first_index+1)
            return True
    return False

def merge(intervals):
        intervals.sort()
        current = 0
        while True:
            if(current == len(intervals)-1):
                break
            merged = mergeTwoIntervals(intervals,current)
            if(merged == False):
                current = current + 1
        return intervals

'''

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)
    return merged
