# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def get_grade(self):
#         return self.grade
#
#
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             print("student added")
#         else:
#             print("maxed")
#
# s1 = Student("Jason", 18, 90)
# s2 = Student("Tim", 18, 90)
# c = Course("IT", 1)
#
# c.add_student(s1)
# print(c.students[0].name + str(c.students[0].age))


# How do you find the missing number in a given integer array of 1 to 100?
lst = [1, 5, 6, 50, 80, 99, 100]
missing = []
for x in range(1, 100):
    if x not in lst:
        missing.append(x)
print(missing)


# How do you find the duplicate number on a given integer array?
lst = [1, 5, 6, 6, 8, 8, 50, 80, 99, 100]
check = []
duplicate = []
for x in lst:
    if x not in check:
        check.append(x)
    else:
        duplicate.append(x)

print(duplicate)


# How do you find the largest and smallest number in an unsorted integer array?
lst = [1, 5, 7, 6, 9, 8, 4, 80, 3, 11]
print(max(lst), min(lst))


# How do you find all pairs of an integer array whose sum is equal to a given number?
lst = [2, 6, 3, 9, 11, 5]
sum = 11
pair = []

for x in lst:
    diff = sum - x
    if diff in lst:
        pair.append(diff)


# How do you find duplicate numbers in an array if it contains multiple duplicates?
lst = [1, 1, 1, 2, 3, 3, 4, 5, 5]
unique = []

for x in lst:
    if x not in unique:
        unique.append(x)
for x in unique:
    count = 0
    for y in lst:
        if x == y:
            count += 1
    if count > 1:
        print([x])


