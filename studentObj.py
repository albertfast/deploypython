import json
import os

class Student:
    """
    Class to represent a Student with personal details.
    Includes methods to initialize, input, and print student information.
    """

    def __init__(self, name=None, address=None, city=None, state=None, zip_code=None, student_id=None, gpa=None):
        """
        Initializes a Student object with default values as None.
        """
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code
        self.student_id = student_id
        self.gpa = gpa

    def to_dict(self):
        """
        Converts the Student object to a dictionary for saving to a file.
        """
        return {
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip,
            "student_id": self.student_id,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Student object from a dictionary.
        """
        return cls(
            name=data["name"],
            address=data["address"],
            city=data["city"],
            state=data["state"],
            zip_code=data["zip_code"],
            student_id=data["student_id"],
            gpa=data["gpa"],
        )

    def printOutput(self):
        """
        Prints the student's details in a nicely formatted manner.
        """
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"ZIP Code: {self.zip}")
        print(f"Student ID: {self.student_id}")
        print(f"GPA: {self.gpa:.2f}")


# Dosya Yolu
FILE_PATH = "students.json"

# Öğrencileri JSON dosyasına kaydet
def save_students_to_file(students):
    with open(FILE_PATH, "w") as file:
        json.dump([student.to_dict() for student in students], file, indent=4)

# JSON dosyasından öğrencileri yükle
def load_students_from_file():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        data = json.load(file)
        return [Student.from_dict(item) for item in data]

# Ana Program
print("Welcome to the Student Management System!")

# JSON dosyasından mevcut öğrencileri yükle
students = load_students_from_file()

# Mevcut initial_student ve test_data
initial_student = {
    "name": "Albert Python",
    "address": "123 main st.",
    "city": "San Francisco",
    "state": "CA",
    "zip_code": "96358",
    "student_id": "W2535",
    "gpa": 4,
}

# Test verileri
test_data = [
    {
        "name": f"Student {i} Name" if i > 1 else initial_student["name"],
        "address": f"Address {i}" if i > 1 else initial_student["address"],
        "city": f"City {i}" if i > 1 else initial_student["city"],
        "state": "CA",
        "zip_code": f"9000{i}" if i > 1 else initial_student["zip_code"],
        "student_id": f"S{i}ID" if i > 1 else initial_student["student_id"],
        "gpa": 3.5 + (i - 1) * 0.1 if i > 1 else initial_student["gpa"],
    }
    for i in range(1, 4)  # 3 öğrenci için döngü
]

# Toplu olarak eklemek istediğiniz yeni öğrenci verileri
bulk_input = [
    {
        "name": "Jane Doe",
        "address": "456 Elm St",
        "city": "Los Angeles",
        "state": "CA",
        "zip_code": "90001",
        "student_id": "JD123",
        "gpa": 3.9,
    },
    {
        "name": "John Smith",
        "address": "789 Oak St",
        "city": "New York",
        "state": "NY",
        "zip_code": "10001",
        "student_id": "JS456",
        "gpa": 3.7,
    },
]

# Öğrenci nesnelerini oluştur
students = [Student(**data) for data in test_data]

# Toplu girdiyi öğrenciler listesine ekle
students += [Student(**data) for data in bulk_input]

# Öğrenci bilgilerini yazdır
print("\n==== Students Information ====")
for idx, student in enumerate(students, start=1):
    print(f"\n==== Student {idx} Details ====")
    student.printOutput()


# print("\n==== Students Information ====")
# for idx, student in enumerate(students, start=1):
#     print(f"\n==== Student {idx} Details ====")
#     student.printOutput()

# Yeni öğrenciler eklemek için
while True:
    add_more = input("\nDo you want to add a new student? (yes/no): ").strip().lower()
    if add_more == "no":
        break
    elif add_more == "yes":
        student = Student(
            name=input("Enter Name: ").strip().title(),
            address=input("Enter Address: ").strip(),
            city=input("Enter City: ").strip().title(),
            state=input("Enter State: ").strip().upper(),
            zip_code=input("Enter ZIP Code: ").strip(),
            student_id=input("Enter Student ID: ").strip().upper(),
            gpa=float(input("Enter GPA (0.0 - 4.0): ").strip()),
        )
        students.append(student)
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

# Öğrencileri JSON dosyasına kaydet
save_students_to_file(students)

print("\nUpdated Students List Saved!")

print(students)




