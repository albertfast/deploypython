def get_room_area():
    # Get the dimensions of the room
    length = float(input("Enter the length of the room in feet: "))
    width = float(input("Enter the width of the room in feet: "))
    
    # Calculate the area of the room
    area = length * width
    
    # Return the calculated area
    return area

def calculate_house_area():
    total_area = 0
    room_counter = 0
    
    while True:
        # Get the area of the next room
        room_area = get_room_area()
        
        # Add the room's area to the total area
        total_area += room_area
        
        # Increment the room counter
        room_counter += 1
        
        # Ask if the user wants to add another room
        another_room = input("Do you want to add another room? (yes/no): ").strip().lower()
        if another_room != "yes":
            break
    
    # Output the total area of the house
    print(f"The area of a house with {room_counter} room(s) is {total_area} square feet.")

# Run the function to calculate the house area
calculate_house_area()
