# Given lists
A = [1, 2, 3, 4, 5]
B = [2, 4, 6, 8, 10]

# 1. List comprehension to multiply all elements in A by 7
# This list comprehension iterates over each element 'x' in list A and multiplies it by 7.
# The resulting list is stored in variable S.
S = [x * 7 for x in A]
print("S is", S)

# 2. List comprehension to find unique even elements in both A and B
# This list comprehension iterates over each element 'x' in the combined list (A + B).
# It checks if 'x' is even by using the condition (x % 2 == 0). If true, it adds 'x' to the set.
# The use of set ensures that only unique values are kept.
Even = sorted(list({x for x in A + B if x % 2 == 0}))
# The 'sorted()' function is used to make sure the final list is in ascending order.
# The 'list()' function converts the set back into a list format for printing.
print("Even is", Even)

# 3. List comprehension to multiply each element in A with each element in B
# This nested list comprehension iterates over each element 'a' in A and each element 'b' in B.
# It multiplies 'a' by 'b' and adds the result to the 'multiples' list.
multiples = [a * b for a in A for b in B]
print("multiples is", multiples)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev forward
            current = next_node  # Move current forward

        return prev

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert linked list to a list for easier validation
def linked_list_to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values

# For testing on the platform:
if __name__ == "__main__":
    # Example input (you can adjust based on test case):
    head_values = [1, 2, 3, 4, 5]  # Modify this dynamically for the test cases
    head = create_linked_list(head_values)

    # Reverse the linked list
    solution = Solution()
    reversed_head = solution.reverseList(head)

    # Convert the reversed list back to a Python list for output
    print(linked_list_to_list(reversed_head))
