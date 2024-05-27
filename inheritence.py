class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Student(Person):
    def __init__(self, name, age, cid_number, student_id):
        super().__init__(name, age, cid_number)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")


class Teacher(Person):
    def __init__(self, name, age, cid_number, employee_id):
        super().__init__(name, age, cid_number)
        self.employee_id = employee_id

    def teach(self):
        print(f"{self.name} is teaching.")


# Creating objects
student1 = Student("karma", 18, "CID11516003375", "S123")
teacher1 = Teacher("sangay", 27, "CID11516003385", "T789")

# Accessing common attributes and behaviors
print(student1.name)
print(teacher1.age)
student1.walk()
teacher1.talk()

# Accessing specific attributes and behaviors
print(student1.student_id)
print(teacher1.employee_id)
student1.study()
teacher1.teach()