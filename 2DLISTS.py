newcart = [ ['apple', 'banana'], ['carrot', 'onion'], ['cookies', 'chips']]

for r in range(len(newcart)):
    for c in range(len(newcart[r])):
        print(newcart[r][c])

for r in range(len(newcart)):
    for c in range(len(newcart[r])):
        print("row:", r, "col:", c, newcart[r][c])