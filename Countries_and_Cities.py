# Understand:
# Given a list of countries and cities of each country, then given the names of the cities.
# For each city print the country in which it is located.

def locate_cities():
    # Step 1: Read the number of countries and strip unnecessary characters
    n = int(input().strip())  # Read the number of countries

    # Step 2: Initialize a dictionary to map cities to their countries
    city_to_country = {}

    # Step 3: Populate the dictionary with cities and their corresponding countries
    for _ in range(n):
        # Read the input line containing a country and its cities, strip unnecessary characters
        data = input().strip().split()  # Split the input into a list
        country = data[0]  # The first word is the country name
        cities = data[1:]  # The remaining words are the cities

        # Map each city to the corresponding country
        for city in cities:
            city_to_country[city] = country

    # Step 4: Read the number of city queries and strip unnecessary characters
    m = int(input().strip())  # Read the number of city queries

    # Step 5: Process each query
    for _ in range(m):
        city = input().strip()  # Read the city name to query, strip unnecessary characters
        print(city_to_country[city])  # Print the country for the queried city

locate_cities()







