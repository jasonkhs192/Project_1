class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print("student added")
        else:
            print("maxed")

s1 = Student("Jason", 18, 90)
s2 = Student("Tim", 18, 90)
c = Course("IT", 1)

c.add_student(s1)
print(c.students[0].name + str(c.students[0].age))
