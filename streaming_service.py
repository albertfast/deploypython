# ===================== UMPIRE ====================
# Understand:
# Problem Statement:
# - The user has a subscription package ('A', 'B', or 'C') and has used a certain number of viewing hours.
# - Based on the hours used, calculate the total cost for the selected package.
# - Additionally, if a different package would result in cost savings, display a message suggesting the potential savings.

# Inputs:
# - package: A character ('A', 'B', or 'C') indicating the package selected by the user.
# - hours: An integer representing the number of hours the user has used.

# Output:
# - Print the calculated cost (price) for the selected package.
# - If another package offers savings, print the potential savings.

# Restrictions:
# - Only valid inputs for `package` are 'A', 'B', and 'C'.
# - Package prices vary based on hours used:
#   - Package A: $8.95 for the first 10 hours, and $1.5 per additional hour.
#   - Package B: $14.95 for the first 20 hours, and $1.0 per additional hour.
#   - Package C: $23.95 for the first 40 hours, and $0.50 per additional hour.

# Match:
# - Utilize conditional statements to calculate prices based on the chosen package and hours.
# - Perform price comparisons with all packages to suggest the most cost-effective option, if any.

# Plan:
# 1. Initialize `price` based on the chosen package.
# 2. Calculate the total cost for each package based on the number of hours used.
# 3. Display the total cost for the chosen package.
# 4. Compare the calculated price with alternative packages and print potential savings if they exist.

# Implementation:
# Get user input for package choice and hours watched
#package = input().strip()    # 'A', 'B', or 'C'. Don't worry about validating the input here.
#hours = int(input())         # An integer between 1 - 744

package = input().strip().upper()
hours = int(input())
price = 0  # Initialize the price variable

# Determine the cost based on the selected package and hours
if package == 'A':
    if hours <= 10:
        # Package A base price for up to 10 hours
        price = 8.95
    else:
        # Additional cost for hours beyond 10 in Package A
        price = 8.95 + (hours - 10) * 1.5
elif package == 'B':
    if hours <= 20:
        # Package B base price for up to 20 hours
        price = 14.95
    else:
        # Additional cost for hours beyond 20 in Package B
        price = 14.95 + (hours - 20) * 1.0
elif package == 'C':
    if hours <= 40:
        # Package C base price for up to 40 hours
        price = 23.95
    else:
        # Additional cost for hours beyond 40 in Package C
        price = 23.95 + (hours - 40) * 0.50
else:
    # Invalid package selection
    print('Invalid Choice')
    price = None

# Display the calculated price if a valid package was selected
if price is not None:
    print(f"Amount Due: ${price:.2f}")

# Calculate the cost for each package and offer a savings suggestion if applicable
if price is not None:
    # Calculate costs for each package
    price_A = 8.95 if hours <= 10 else 8.95 + (hours - 10) * 1.5
    price_B = 14.95 if hours <= 20 else 14.95 + (hours - 20) * 1.0
    price_C = 23.95 if hours <= 40 else 23.95 + (hours - 40) * 0.50

    # Find the minimum price among all packages
    prices = {'A': price_A, 'B': price_B, 'C': price_C}
    best_package = min(prices, key=prices.get)
    best_price = prices[best_package]

    # Suggest only if switching saves money
    if best_price < price:
        savings = price - best_price
        print(f"You could save ${savings:.2f} by switching to package {best_package}")
'''
package = str(input("Package choice (A, B, or C): "))
hours = int(input("Hours: "))
price = 0  # Başlangıçta fiyatı 0 olarak ayarlıyoruz

if package == 'A':
    if hours <= 10:
        price = 8.95
    else:
        price = 8.95 + (hours - 10) * 1.5
elif package == 'B':
    if hours <= 20:
        price = 14.95
    else:
        price = 14.95 + (hours - 20) * 1.0
elif package == 'C':
    if hours <= 40:
        price = 23.95
    else:
        price = 23.95 + (hours - 40) * 0.50
else:
    print('Invalid Choice')
    price = None  # Geçersiz seçim yapıldığında price None olur

if price is not None:
    print("Price:", price)
'''
