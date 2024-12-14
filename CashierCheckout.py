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

# Define prices and initialize counters
items = {
    "Apple": {"price": 2.20, "count":0},
    "Orange": {"price": 3.40, "count":0},
    "Banana": {"price": 1.50, "count":0},
    "Melon": {"price": 4.10, "count":0}
}
total = 0

# Start scanning items
while True:
    scanned_item = input()

    if scanned_item == "CHECKOUT":
        # Print subtotal for each item and the grand total
        for item, info in items.items():
            if info["count"] > 0:
                item_total = info["count"] * info["price"]
                print(f"{item}: ${item_total:.2f}")
        print(f"Total: ${total:.2f}")
        break

    elif scanned_item in items:
        items[scanned_item]["count"] += 1
        total += items[scanned_item]["price"]
    else:
        print("Invalid Item")





















