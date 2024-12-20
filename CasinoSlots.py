# Purpose: Practice while loops & infinite loops
# Problem Statement:
# Write a program that will simulate a slot machine.

# The user will receive a prompt to enter a bet: "Bet: "
# The program will then generate 3 random numbers, each representing a slot
# If two numbers in a row match, double their bet
# If all three numbers match, triple their bet
# If all three numbers are 7s, septuple (7x) their bet
# Otherwise, the player loses their bet
# Print the casino slots (3 numbers) and the result of the bet. When the player inputs "DONE", print the amount gained/lost and end the program.

# Note on random numbers: Python can generate random numbers using the random module.
# The main function we'll be using is random.randint()Links to an external site
# You can create a random number with random.randint(minimum_number, maximum_number).
# You'll note that the first input is used to called an integer. This integer is a seed,
# which makes random numbers generated repeatable between each code execution and allows the CodeCheck tests to work.
# We recommend only making 3 random.randint() calls per iteration.
# Bonus: "The House always wins." Go through 50, 500, then 1,000 bets. Does the House win?


# Example	                      Input	                 Output
# 	                              42 (random seed)
#                                 Bet: 5                   6 1 1 10
#                                 Bet: 5                   6 3 2 -5
#                                 Bet: 5                   2 2 6 10
#                                 Bet: DONE                15

import random
random.seed(int(input()))

total = 0

while True:
    bet_input = input("Bet: ")
    if bet_input.upper() == "DONE":
        print(total)
        break

    bet = int(bet_input)

    slot1 = random.randint(1, 7)
    slot2 = random.randint(1, 7)
    slot3 = random.randint(1, 7)


    print(f"{slot1} {slot2} {slot3} ", end="") # Added a space after the slot numbers

    if slot1 == slot2 == slot3:
        if slot1 == 7:  # This condition is now redundant as 7 is out of range
            win = bet * 7
        else:
            win = bet * 3
    elif slot1 == slot2 or slot2 == slot3:
        win = bet * 2
    else:
        win = -bet

    print(win)
    total += win