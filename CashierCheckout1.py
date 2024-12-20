# ================================UMPIRE========================================
# Understand:
#Given a list of grocery items, print a receipt.
#Apples cost $2.20 each
#Bananas cost $1.50 each
#Oranges cost $3.40 each
#Melons cost $4.10 each
#Print subtotals for each category of items, then print the total.

# Example:         Input:              Output:
#                  Apple               Apple:  $2.20
#                  Orange              Orange: $3.40
#                  Banana              Banana: $3.0
#                  Melon               Melon:  $4.10
#                  Banana              Total:  $12.70

# Match:
# 1. Define prices for each item.
# 2. Use counters to keep track of the number of each item scanned.
# 3. Start an input loop to take item names one at a time.
# 4. If "CHECKOUT" is entered, print the subtotal for each item and the total.
# 5. If a valid item is entered, update the respective counter and add the item's price to the total.
# 6. If an invalid item is entered, display an error message.

# ================================Implementation================================

# Prices of each item
Apple = 2.20
Banana = 1.50
Orange = 3.40
Melon = 4.10

# Initialize counters for each item
apple_count = 0
banana_count = 0
orange_count = 0
melon_count = 0
total = 0

# Start scanning items
while True:
    scanned_item = input()

    # Check if the user wants to print the total
    if scanned_item == "CHECKOUT":
        # Calculate and print subtotal for each item
        if apple_count > 0:
            apple_total = apple_count * Apple
            print(f"Apples: ${apple_total:.2f}")
        if banana_count > 0:
            banana_total = banana_count * Banana
            print(f"Bananas: ${banana_total:.2f}")
        if orange_count > 0:
            orange_total = orange_count * Orange
            print(f"Oranges: ${orange_total:.2f}")
        if melon_count > 0:
            melon_total = melon_count * Melon
            print(f"Melons: ${melon_total:.2f}")

        # Print grand total
        print(f"Total: ${total:.2f}")
        break  # Exit the loop after printing the total

    # Update item count and add to total based on the scanned item
    elif scanned_item == "Apple":
        apple_count += 1
        total += Apple
        continue
    elif scanned_item == "Banana":
        banana_count += 1
        total += Banana
        continue
    elif scanned_item == "Orange":
        orange_count += 1
        total += Orange
        continue
    elif scanned_item == "Melon":
        melon_count += 1
        total += Melon
        continue
    else:
        print("Invalid Item")
