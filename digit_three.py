# Input: A three-digit integer
X = int(input("Enter a three-digit integer with unique digits: "))

# Ensure X is a three-digit integer with unique digits
if 100 <= X <= 999:
    # Extract digits
    hundreds = X // 100           # Extract hundreds place
    tens = (X // 10) % 10         # Extract tens place
    units = X % 10                # Extract units place

    # Check if all digits are unique and in increasing order
    if hundreds != tens and tens != units and hundreds != units and hundreds < tens < units:
        print("YES")
    else:
        print("NO")
else:
    print("NO")  # If X is not a three-digit integer, output NO
