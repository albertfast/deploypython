a = [ 3, 5]
xor_out = a[0] ^ a[1]
print(xor_out)

a = [ 3, 3]
xor_out = a[0] ^ a[1]
print(xor_out)

a = [ 3, 3, 5]
xor_out = a[0] ^ a[1] ^ a[2]
print(xor_out)

a = [ 3, 5, 5]
xor_out = a[0] ^ a[1] ^ a[2]
print(xor_out)


a = [ 3, 3, 5, 4, 4]
xor_out = 0
for i in a:
    xor_out = xor_out ^ i;
print(xor_out)

a = [ 1020, -110, 45, 1020, -110 ]
xor_out = 0
for i in a:
    xor_out = xor_out ^ i;
print(xor_out)