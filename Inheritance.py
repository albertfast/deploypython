# Üst Sınıf (Parent Class)
class Fruit:
    def __init__(self, color, flavor):
        self.color = color  # Renk özelliği
        self.flavor = flavor  # Tat özelliği

# Alt Sınıflar (Child Classes)
class Apple(Fruit):
    pass  # Ek bir özellik ya da yöntem eklenmemiş

class Grape(Fruit):
    pass  # Ek bir özellik ya da yöntem eklenmemiş

# Nesnelerin Oluşturulması
granny_smith = Apple("green", "tart")  # Yeşil ve ekşi bir elma
carnelian = Grape("purple", "sweet")  # Mor ve tatlı bir üzüm

# Veriye Erişim
print(granny_smith.flavor)  # Çıktı: tart
print(carnelian.color)  # Çıktı: purple


# Üst Sınıf (Parent Class)
class Animal:
    sound = ""  # Hayvanların sesi

    def __init__(self, name):
        self.name = name  # Hayvanın adı

    def speak(self):
        # Hayvanın adını ve sesini ekrana yazdırır
        print("{sound} I'm {name}! {sound}".format(
            name=self.name, sound=self.sound
        ))

# Alt Sınıf: Domuzcuk (Piglet)
class Piglet(Animal):
    sound = "Oink!"  # Domuzların sesi

# Alt Sınıf: İnek (Cow)
class Cow(Animal):
    sound = "Moooo"  # İneklerin sesi

# Örnek Kullanım
hamlet = Piglet("Hamlet")  # Bir Piglet nesnesi oluştur
hamlet.speak()  # Çıktı: "Oink! I'm Hamlet! Oink!"

milky = Cow("Milky White")  # Bir Cow nesnesi oluştur
milky.speak()  # Çıktı: "Moooo I'm Milky White! Moooo"


# Class to represent a Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Overloading the + operator to add the radii of two circles
    def __add__(self, other):
        return Circle(self.radius + other.radius)  # Combine radii

    def __str__(self):
        return f"Circle with radius {self.radius}"  # String representation

# Create two Circle objects
circle1 = Circle(5)
circle2 = Circle(7)

# Use the overloaded + operator
circle3 = circle1 + circle2

print(circle1)  # Output: "Circle with radius 5"
print(circle2)  # Output: "Circle with radius 7"
print(circle3)  # Output: "Circle with radius 12"

