class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name

def main():
    student1 = Student("Brenzo")
    student2 = Student("Jerry")
    student3 = Student("Reian")

    print("Equality test:")
    print(f"{student1.name} == {student2.name}: {student1 == student2}")
    print(f"{student1.name} == {student3.name}: {student1 == student3}")
    print()

    print("Less than test:")
    print(f"{student1.name} < {student2.name}: {student1 < student2}")
    print(f"{student1.name} < {student3.name}: {student1 < student3}")
    print()

    print("Greater than or equal to test:")
    print(f"{student1.name} >= {student2.name}: {student1 >= student2}")
    print(f"{student1.name} >= {student3.name}: {student1 >= student3}")

if __name__ == "__main__":
    main()
