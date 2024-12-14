# ===================== Umpire Process ====================

# Understand:
# Given:
# - A cupcake costs A dollars and B cents.
# - We need to determine how much the total cost will be for N cupcakes.
# - The output should be in dollars and cents.
#
# Input:
# - Three integers: A (dollars per cupcake), B (cents per cupcake), and N (number of cupcakes).
#
# Output:
# - Total cost in two integers: total dollars and remaining cents.

# Plan:
# 1. Convert the price of one cupcake into total cents (A * 100 + B).
# 2. Multiply this total cents value by the number of cupcakes, N, to get the overall cost in cents.
# 3. Convert the total cents back into dollars and cents:
#    - Use integer division to get the dollar amount.
#    - Use modulus to get the remaining cents.

# Implementation:

# Get inputs
A = int(input("Enter dollars per cupcake: "))  # Dollar part of the price per cupcake
B = int(input("Enter cents per cupcake: "))    # Cents part of the price per cupcake
N = int(input("Enter number of cupcakes: "))   # Number of cupcakes

# Step 1: Calculate the price of one cupcake in cents
price_per_cupcake_cents = A * 100 + B  # Convert dollars to cents and add to cents

# Step 2: Calculate the total cost in cents for N cupcakes
total_cost_cents = price_per_cupcake_cents * N  # Total cost in cents

# Step 3: Convert total cents to dollars and cents
total_dollars = total_cost_cents // 100         # Dollar part
remaining_cents = total_cost_cents % 100        # Remaining cents part

# Output the result
print(total_dollars, remaining_cents)

# Example:
# If A = 2, B = 50, and N = 4, then:
# - price_per_cupcake_cents = 2 * 100 + 50 = 250
# - total_cost_cents = 250 * 4 = 1000
# - total_dollars = 1000 // 100 = 10
# - remaining_cents = 1000 % 100 = 0
# Output: 10 0
