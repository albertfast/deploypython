# ================================UMPIRE========================================
# Understand:
# Given a collection of two intervals, check if they are overlapping and return the overlapping intervals.
#
# Example 1:
#
# Given a list of intervals[1,3],[2,6],
#
# return a list of intervals [1,6]
#
# Example 2:
#
# Given a list of intervals [1,3],[4,6],
#
# return a list of intervals [1,3],[4,6]
#
# You can assume the input intervals are sorted.

# Understand:
# The task is to merge two intervals if they overlap and are sorted.
# If the intervals do not overlap, return them as separate intervals.
# Input consists of two intervals, each with a start and end value.
# Example 1: Input: [1, 3], [2, 6] → Output: [1, 6]
# Example 2: Input: [1, 3], [4, 6] → Output: [1, 3], [4, 6]

# Restriction:
# - Input must always contain exactly two intervals.
# - Intervals must be sorted in ascending order by their start times.
# - No advanced libraries should be used for solving this problem.
# - Output should match the format as described (merged if overlapping, otherwise separate).

# Match:
# - Problem involves understanding overlapping conditions of intervals.
# - Similar problems include range merging and scheduling conflicts.
# - Use conditional statements (if-else) to check overlap.
# - Use a simple loop to parse input for two intervals.
# - Requires sorting validation and a basic comparison to merge.

# Plan:
# 1. Take User input
# 2. Read the input directly as two intervals (each with start and end values).
# 3. Validate that the intervals are sorted (i.e., the first interval starts earlier).
# 4. Check if the intervals overlap:
#    - If overlapping, merge them by taking the smaller start value and the larger end value.
#    - If not overlapping, output both intervals separately.
# 5. Print the result in the specified format.



# Implementation
def merge_intervals(intervals):
    x1 = intervals[0][0]
    x2 = intervals[0][1]
    y1 = intervals[1][0]
    y2 = intervals[1][1]
    if (y1 <= x2):
        if(y2 < x2):
            return [[x1, x2]]
        else:
            return [[x1, y2]]
    else:
        return [[x1, x2], [y1, y2]]

if __name__ == "__main__":
    # Kullanıcıdan input alınması
    print("Enter two intervals (start and end values separated by space, e.g., '1 3', '2 6'):")
    try:
        # İlk interval
        x1, x2 = map(int, input("First interval: ").split())
        # İkinci interval
        y1, y2 = map(int, input("Second interval: ").split())
        # Interval listesini oluşturma
        intervals = [[x1, x2], [y1, y2]]
    except ValueError:
        print("Invalid input. Please enter valid intervals in the format 'start end'.")
        exit()

    # merge_intervals fonksiyonunu çağırma ve sonucu yazdırma
    result = merge_intervals(intervals)
    print("Result:", result)
    
# Review:
# The given code is designed to merge two intervals if they overlap and assumes that
# the input intervals are already sorted. Below are the observations:

# 1. **Function Design:**
#    - The function mergeIntervalI is well-structured and straightforward.
#    - It takes a single input intervals, which is expected to be a 2D array (e.g., [[1, 3], [4, 6]]).

# 2. **Handling Overlap:**
#    - The condition if (y1 <= x2) checks for overlap between the intervals.
#    - Nested conditions ensure that the intervals are merged correctly if they overlap.

# 3. **Handling Separate Intervals:**
#    - If the intervals do not overlap, they are returned as separate intervals using the else block.

# 4. **Assumptions:**
#    - Assumes that the input intervals are sorted, so no additional sorting logic is needed.
#    - Relies on the system (LMS) to provide exactly two valid input intervals.

# Evaluate:
# 1. **Correctness:**
#    - The code handles overlapping intervals correctly:
#      Example 1: Input: [[1, 3], [2, 6]] → Output: [[1, 6]]
#    - The code handles non-overlapping intervals correctly:
#      Example 2: Input: [[1, 3], [4, 6]] → Output: [[1, 3], [4, 6]]

# 2. **Efficiency:**
#    - The function operates in constant time O(1) since it only evaluates conditions on two intervals.
#    - This makes it highly efficient for the given scope.

# 3. **Reliability:**
#    - The code assumes sorted input and does not validate the input.
#    - It works correctly as long as the input matches the expected format and constraints.

# 4. **Scalability:**
#    - The function is limited to handling exactly two intervals. It cannot handle more than two intervals
#      without significant modification.

# 5. **Maintainability:**
#    - The function is simple and easy to understand, which makes it maintainable.
#    - However, adding support for more intervals would require a redesign.

# Conclusion:
# - The code is optimal for the specific use case of merging exactly two sorted intervals.
# - It would fail or produce incorrect results if the input format is incorrect or contains more than two intervals.
# - For broader use cases, enhancements like input validation and support for more intervals would be necessary.



