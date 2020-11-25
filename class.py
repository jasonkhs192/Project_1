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

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Jason", "Kim", 50000)
emp_2 = Employee("James", "Lee", 40000)

Employee.set_raise_amt(2.42)
emp_1.apply_raise()
print(emp_1.pay)