'''
password = "12345!"
x = input("Give me the password: ")
while x != password:
    x = input("Wrong password. Give me the password: ")
'''
n = input("Enter our first number: ")
sum = 0
counter = 0  # Giriş sayısını tutmak için sayaç oluşturuyoruz

while n != "":
    sum += int(n)
    counter += 1  # Her girdi aldığınızda sayaç bir artırılır
    if counter == 3:  # Eğer 3 giriş alındıysa döngüyü sonlandırır #break
        print(sum)
    n = input("Enter next number: ")

print("Sum:", sum)


i = 0

while i < 10:
    if i == 2:
        print(f"Skipping {i} (continue)")
        i += 1  # Continue sonrası adım atlamak için i'yi artırıyoruz
        continue
    if i == 8:
        print(f"Breaking at {i} (break)")
        break
    print(f"Current value of i: {i}")
    i += 1

print("Loop ended")

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
    scanned_item = input("Enter the scanned item (or type 'Total' to finish): ")

    # Check if the user wants to print the total
    if scanned_item == "Total":
        print("\nReceipt:")

        # Calculate and print subtotal for each item
        if apple_count > 0:
            apple_total = apple_count * Apple
            print(f"Apple:  ${apple_total:.2f} ({apple_count} @ ${Apple:.2f} each)")
        if banana_count > 0:
            banana_total = banana_count * Banana
            print(f"Banana: ${banana_total:.2f} ({banana_count} @ ${Banana:.2f} each)")
        if orange_count > 0:
            orange_total = orange_count * Orange
            print(f"Orange: ${orange_total:.2f} ({orange_count} @ ${Orange:.2f} each)")
        if melon_count > 0:
            melon_total = melon_count * Melon
            print(f"Melon:  ${melon_total:.2f} ({melon_count} @ ${Melon:.2f} each)")

        # Print grand total
        print(f"Total:  ${total:.2f}")
        break  # Exit the loop after printing the total

    # Update item count and add to total based on the scanned item
    elif scanned_item == "Apple":
        apple_count += 1
        total += Apple
    elif scanned_item == "Banana":
        banana_count += 1
        total += Banana
    elif scanned_item == "Orange":
        orange_count += 1
        total += Orange
    elif scanned_item == "Melon":
        melon_count += 1
        total += Melon
    else:
        print("Invalid Item")

