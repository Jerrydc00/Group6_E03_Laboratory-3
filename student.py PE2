import random 

class Student:
    def __init__(self, first_name, last_name, sex, age, student_number):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.student_number = student_number
        self.name = first_name  # For sorting by name

    def __eq__(self, other):
        return self.first_name == other.first_name

    def __lt__(self, other):
        return self.first_name < other.first_name

    def __ge__(self, other):
        return self.first_name >= other.first_name

    def __str__(self):
        return (f"Name: {self.first_name} {self.last_name}, "
                f"Sex: {self.sex}, Age: {self.age}, "
                f"Student Number: {self.student_number}")

def main():
    # Create a list of Student objects
    students = [
        Student("Brenzo", "Venida", "M", 19, "2023102590"),
        Student("Jerry", "Dela Cruz", "M", 20, "2021135637"),
        Student("Reian", "Labrador", "M", 20, "2022105662"),
        Student("Jonathan", "Taylar", "M", 40, "2020123456"),
        Student("Mel", "Noxus", "F", 28, "2016456789"),
    ]
    
    # Shuffle the list to randomize the order
    random.shuffle(students)

    # Display the shuffled order
    print("Shuffled List:")
    for student in students:
        print(student)
    print()

    # Sort the list based on the first name
    students.sort()

    # Display the sorted list
    print("Sorted List:")
    for student in students:
        print(student)

if __name__ == "__main__":
    main()
