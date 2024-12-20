s = "Accelerate"
s1 = "Accelerate!"
s2 = "CTI Accelerate One Two Three"
a,b,c,d,e = s2.split()
f = s2.split()
s3 = "Racecar"
s4 = "Racecar!"

print(s[:-1])        # Accelerat
print(s)             # Accelerate
print(s[-1])         # e
print(s[-2:len(s)])  # te
print(len(s)//2)     # 5
print(len(s))        # 10
print(s1[0:(len(s1)//2)]) # Accel
print(s1[len(s1)-1]) # !
print(a)             # CTI
print(b)             # Accelerate
print(d)             # Two
print(f[4])          # Three
print(s1[::-1])      # !etareleccA

for ch in s3:
    print(ch)

for x in range(len(s4)):
    print(s4[x], end="")







