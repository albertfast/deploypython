x = {1,2,3}
y = set([3,4,5])
print(x,y) # {1, 2, 3} {3, 4, 5}
print(x | y) # {1, 2, 3, 4, 5}
print(x & y) # {3}
print(x ^ y) # {1, 2, 4, 5}
print(x - y) # {1, 2}

x = [23, 93, 7, 33, 23, 7, 42, 33, 93]

# XOR kullanarak tekrar etmeyen sayıyı bulma
result = 0
for num in x:
    result ^= num  # XOR işlemi

print(f"Tekrar etmeyen sayı: {result}")

z = [53, 93, 7, 43, 53, 7, 42, 43, 93]
once = set()
twice = set()
for num in z:
    if num not in once:
        once.add(num)
    else:
        twice.add(num)
print(once, twice) # {7, 42, 43, 53, 93} {43, 93, 53, 7}
print(once - twice) # {42}
print(once ^ twice) # {42}
print(once & twice) # {53, 43, 93, 7}
print(once | twice) # {7, 42, 43, 53, 93}

y = set()
for i in [23, 33, 33, 91, 23, 7]:
    y ^= {i}
print(y) # {91, 7} # Same Time complexity & worse space complexity

x = "try something new every now and then"
y = "every day something new happen"

x = set(x.split())
y = set(y.split())
print(x,y) # {'now', 'every', 'try', 'new', 'and', 'something', 'then'} {'happen', 'every', 'day', 'new', 'something'}
print(x & y) # {'something', 'new', 'every'}


print(len(set(map(int, input().split())))) # input: 10 10 4 2 5 5 10 4 1 10 output: 5

x = input() # 1 2 3 4 5 5 7
y = input() # 5 7 8 9 10 11 12
x = set(x.split())
y = set(y.split())
intersection = sorted([int(num) for num in x & y])
for num in intersection:
    print(num, end=" ") # 5 7


numbers = input().split() # 1 2 3 2 3 4
seen = set()              #    NO
                          #    NO
for num in numbers:       #    NO
    if num in seen:       #    YES
        print("YES")      #    YES
    else:                 #    NO
        print("NO")
        seen.add(num)












