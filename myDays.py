from datetime import datetime

# Get user input for date of birth and assignment due date
dob_input = input("Enter your Birth Day (YYYY-MM-DD): ")
due_date_input = input("Enter Assignment Due Date (YYYY-MM-DD): ")

# Convert the input strings to datetime objects
dob = datetime.strptime(dob_input, "%Y-%m-%d")
due_date = datetime.strptime(due_date_input, "%Y-%m-%d")

# Calculate the number of years lived including birth year and current year
years_lived = due_date.year - dob.year + 1  # Include both birth year and current year
# Check if the birth date is more than 10 years ago and less than 100 years ago
if years_lived < 10 or years_lived > 100:
    print(
        "Error: The birth date must be more than 10 years ago and less than 100 years ago."
    )
else:

    # Function to check if a year is a leap year
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Calculate the number of leap years in the lived years
leap_years = sum(is_leap_year(year) for year in range(dob.year, due_date.year + 1))

# Calculate the number of days in the birth year before the birth date
days_in_birth_year = (dob - datetime(dob.year, 1, 1)).days + 1

# Calculate the number of days remaining in the current year after the due date
days_remaining_in_current_year = (datetime(due_date.year, 12, 31) - due_date).days

# Initialize total days lived to zero
days = 0
# Add the days from the full years lived (365 days per year)
days += years_lived * 365
# Add the extra days for leap years
days += leap_years
# Subtract the days in the birth year before the birth date
days -= days_in_birth_year
# Subtract the days remaining in the current year after the due date
days -= days_remaining_in_current_year

# Print the results
print(f"DOB: {dob.strftime('%B %d, %Y')}")  # Print the date of birth
print(f"Due: {due_date.strftime('%B %d, %Y')}")  # Print the assignment due date
print(f"Years lived: {years_lived} years")  # Print the number of years lived
print(f"Leap years: {leap_years} leap years")  # Print the number of leap years
print(
    f"Days in birth year before birth: {days_in_birth_year} days"
)  # Print the days in birth year before the birth date
print(
    f"Days remaining in current year after due date: {days_remaining_in_current_year} days"
)  # Print the days remaining in the current year after the due date
print(f"Age: {days} days")  # Print the total age in days
