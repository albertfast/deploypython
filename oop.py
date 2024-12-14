# import math
#
# # Altın Oran ifadesi
# phi = (1 + math.sqrt(5)) / 2
#
# # Phi'nin 12. kuvveti
# result = phi ** 12
#
# # Sonucu yazdır
# print(result)

###################################

# import datetime
#
# class User:
#     """A member of FriendFace. For now we are only storing their name and birthday.
#     But soon we will store an uncomfortable amount of user information."""
#
#     def __init__(self, full_name, birthday):
#         self.name = full_name
#         self.birthday = birthday  # yyyymmdd
#
#         # Extract first and last names
#         name_pieces = full_name.split(" ")
#         self.first_name = name_pieces[0]
#         self.last_name = name_pieces[-1]
#
#     def age(self):
#         """Return the age of the user in years."""
#         today = datetime.date(2001, 5, 12)
#         yyyy = int(self.birthday[0:4])
#         mm = int(self.birthday[4:6])
#         dd = int(self.birthday[6:8])
#         dob = datetime.date(yyyy, mm, dd)  # Date of birth
#         age_in_days = (today - dob).days
#         age_in_years = age_in_days / 365
#         return int(age_in_years)
#
# user = User("Dave Bowman", "19710315")
# print(user.age())

class Sales:
    def __init__(self, id):
        self.id = id
        id = 100

val = Sales(123)
print (val.id)  # ==> Output: 123

class People():

    def __init__(self, name):
      self.name = name

    def namePrint(self):
      print("Name: " + self.name)

person1 = People("Sally")
person2 = People("Louise")
person1.namePrint()


class Student:

	def __init__(self,name,id):

		self.name=name

		self.id=id

		print(self.id)

std=Student("Simon",1)

std.id=2

print(std.id)

class A():

	def __init__(self,count=100):

		self.count=count



obj1=A()

obj2=A(102)

print(obj1.count)

print(obj2.count)


class A:

	def __init__(self,num):

		num=3

		self.num=num

	def change(self):

		self.num=7

a=A(5)

print(a.num)

a.change()

print(a.num)
