def SayHello(name):
   print ("Hi {}! How are you?".format(name))
   return

def sum(x,y):
   return x+y

def average(x,y):
   return (x+y)/2

def power(x,y):
   return x**y

texts = ['python', 'javascript', 'html', 'css']
def playText():
   capitalized = [x.title() for x in texts]
   lengths = [len(text) for text in texts]
   print("The texts list each element is Converted to first Letter Capitalized = " ,capitalized)
   print("The texts list each element lengths is = " ,lengths)

concon = 1750
def laddMoney():
   # Uncomment the following line to fix the code:
   global concon
   concon = concon - 250

print ("Actual laddMoney = ",concon)
laddMoney()
print ("Increase laddMoney = ",concon)

Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1

print ("Actual Money = ",Money)
AddMoney()
print ("Increase Money = ",Money)

ages = [5, 12, 17, 18, 24, 32]

def filterAges(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(filterAges, ages)

for x in adults:
  print("Filtered ages = ",x)

min = (lambda x, y: x if x < y else y)
print(min(101*99, 102*98))
L = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
for f in L:
   print(f(3))

y = 6
z = lambda x: x * y
print(z(8))

