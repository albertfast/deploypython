# File: callStudentInfo.py
from student_info_manager1 import collect_student_info



def main():
    print("Welcome to the student information collection program!")
    student_data = collect_student_info()
    print("\nHere is the collected student information:")
    for key, value in student_data.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
