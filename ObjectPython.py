class Apple:
    color = ""
    flavor = ""

    def __str__(self):
        return f"Apple(color={self.color}, flavor={self.flavor})"

# Örnek Kullanım
jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"

golden = Apple()
golden.color = "green"
golden.flavor = "soft"

print(jonagold)  # Apple(color=red, flavor=sweet)
print(golden)    # Apple(color=green, flavor=soft)

# class Piglet:
#     years = 0
#
#     def pig_years(self):
#         return self.years * 18
#
# # Örnek kullanım
# piggy = Piglet()
# print(piggy.pig_years())  # Çıktı: 0
#
# piggy.years = 2
# print(piggy.pig_years())  # Çıktı: 36

class Piglet:
    """Represents a piglet that can say its name and calculate its age in pig years."""

    years = 0  # Piglet'in yaşı
    name = ""  # Piglet'in adı

    def speak(self):
        """Outputs a message including the name of the piglet."""
        print("Oink! I'm {}! Oink!".format(self.name))

    def pig_years(self):
        """Converts the current age to equivalent pig years."""
        return self.years * 18

# Örnek Kullanım
piggy = Piglet()
piggy.name = "Piggy"
piggy.years = 2

# Piglet sınıfının dokümantasyonuna erişmek için help() kullanımı
help(Piglet)

# Piglet sınıfındaki speak metodunun çalıştırılması
piggy.speak()  # Çıktı: Oink! I'm Piggy! Oink!

# Piglet'in yaşını pig yıllarına çevirme
print(piggy.pig_years())  # Çıktı: 36


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

# Örnek Kullanım
tesla = Car("Tesla", "Model S", 2022)
bmw = Car("BMW", "i8", 2021)

print(tesla)  # Çıktı: 2022 Tesla Model S
print(bmw)    # Çıktı: 2021 BMW i8
print()


class test:
    def __init__(self, a="Hello World"):
        self.a = a

    def display(self):
        print(self.a)


obj = test()
obj.display()


class change:
    def __init__(self, x, y, z):
        self.a = x + y + z


x = change(1, 2, 3)
y = getattr(x, 'a')
setattr(x, 'a', y + 1)
print(x.a)


# class test:
#     def __init__(self, a):
#         self.a = a
#
#     def display(self):
#         print(self.a)
#
#
# obj = test()
# obj.display()  # ==> TypeError: test.__init__() missing 1 required positional argument: 'a'


# class
class Laptop:
   # init method
   def __init__(self, company, model):
      # self
      self.company = company
      self.model = model
# creating instances for the class Laptop
laptop_one = Laptop('Asus', 'ideapad320')
laptop_two = Laptop('Dell', 'inspiron 7000')
# printing the properties of the instances
print(f"Laptop One: {laptop_one.company}")
print(f"Laptop Two: {laptop_two.company}")

########################################3
class learn:
    def __init__(self):
        self.variable = 'Old'
        self.Change(self.variable)
    def Change(self, var):
        var = 'New'
obj=learn()
print(obj.variable)

#################################################
class fruits:
    def __init__(self, price):
        self.price = price


obj = fruits(50)

obj.quantity = 10
obj.bags = 2

print("Fruits", obj.quantity + len(obj.__dict__))

####################################################3
def add(c, k):
    c.test = c.test + 1
    k = k + 1


class A:
    def __init__(self):
        self.test = 0


def main():
    Count = A()
    k = 0

    for i in range(0, 25):
        add(Count, k)
    print("Count.test=", Count.test)
    print("k =", k)

main()

####################################


