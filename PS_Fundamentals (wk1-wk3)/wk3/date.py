#ICA
from datetime import datetime
now = datetime.now()

class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f"{self.__name}, {self.__age}"

    def set_name(self, new_name):
        self.__name = new_name

    @classmethod
    def c_emplyee(cls, name, date_of_birth):
        age = now.year - date_of_birth
        return cls(name, age)


# e1 = Employee("Ali", 23)
# e1.set_name("Ahmed")
# print(e1)

e2 = Employee.c_emplyee("Ahmed", 2000)
print(e2)