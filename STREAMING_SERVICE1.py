'''
You're working for a streaming service company and they're experimenting with a new pricing system.
Customers choose from 1 of 3 packages that are paid monthly. Here's what's included in each package:
Package A: $8.95 for 10 hours of Ad-free streaming, $1.50 for each additional hour
Package B: $14.95 for 20 hours of Ad-free streaming, $1.00 for each additional hour
Package C: $23.95 for 40 hours of Ad-free streaming, $0.50 for each additional hour
Given a package & hours spent streaming, calculate the total cost. If a different plan would cost less,
print a message stating which plan and how much they would save (If plan costs match, prioritize A, then B, then C).
If a different plan wouldn't cost less, don't print a message.
'''
packageChoice = input("Enter package choice (A, B, C): ")
hours = int(input("Enter hours spent streaming: "))


def calculate_cost(package, hours):
    if package == 'A':
        base_cost = 8.95
        extra_hour_cost = 1.5
        included_hours = 10
    elif package == 'B':
        base_cost = 14.95
        extra_hour_cost = 1.0
        included_hours = 20
    elif package == 'C':
        base_cost = 23.95
        extra_hour_cost = 0.5
        included_hours = 40
    else:
        return None

    if hours <= included_hours:
        return base_cost
    else:
        return base_cost + (hours - included_hours) * extra_hour_cost


# Calculate cost for chosen package
chosen_package_cost = calculate_cost(packageChoice, hours)

if chosen_package_cost is None:
    print('Invalid Choice')
else:
    print(f"Amount Due: ${chosen_package_cost:.2f}")

    # Calculate costs for other packages and find cheaper one
    costs = {
        'A': calculate_cost('A', hours),
        'B': calculate_cost('B', hours),
        'C': calculate_cost('C', hours)
    }

    cheapest_package = min(costs, key=costs.get)

    if costs[cheapest_package] < chosen_package_cost:
        savings = chosen_package_cost - costs[cheapest_package]
        print(f"You could save ${savings:.2f} by switching to package {cheapest_package}")
