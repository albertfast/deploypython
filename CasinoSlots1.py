import random
random.seed(int(input("Enter Random Seed: ")))

total = 0

while True:
    bet_input = input("Bet:")
    if bet_input.upper() == "DONE":
        print(total)
        break

    bet = int(bet_input)

    slot1 = random.randint(1,7)
    slot2 = random.randint(1, 7)
    slot3 = random.randint(1, 7)

    print(f"{slot1} {slot2} {slot3} ", end="")

    if slot1 == slot2 == slot3:
        if slot1 == 7:
            win = bet * 7
        else:
            win = bet * 3
    elif slot1 == slot2 or slot2 == slot3:
        win = bet * 2
    else:
        win = -bet

    print(win)
    total += win
