class Employee:
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@slworld.com"

    def fullname(self):
        return self.first +" "+self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

emp_1 = Employee("Jason", "Kim", 50000)
emp_2 = Employee("James", "Lee", 40000)

print(emp_1.)

