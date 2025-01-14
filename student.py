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

    print(student1 == student2)
    print(student1 < student2)
    print(student1 >= student2)

    print(student1 == student3)
    print(student1 < student3)
    print(student1 >= student3)

if __name__ == "__main__":
    main()
