#ICA
class Employee:
    overtime = 0
    overtimeAmount = 0
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    def calculate_emp_salary(self, hours_worked):
        while(hours_worked > 0):

            if (hours_worked > 50):
                self.overtime = hours_worked - 50
                self.overtimeAmount = (self.overtime * (self.emp_salary / 50))
                self.emp_salary += self.overtimeAmount
            break
        else:
            print(f"Sorry, no numbers below zero. You entered {hours_worked}")





    def emp_assign_department(self, emp_department):
        self.emp_department = emp_department
    def print_employee_details(self):
        print(f"The employee Id is {self.emp_id} and his name is {self.emp_name} his salary : {self.emp_salary} on {self.emp_department} department ")
num_employees = int(input("Enter the number of employees: "))

employees = []

for _ in range(num_employees):
    emp_id = input("Enter employee ID: ")
    emp_name = input("Enter employee name: ")
    emp_salary = float(input("Enter employee salary: "))
    emp_department = input("Enter employee department: ")

    e = Employee(emp_id, emp_name, emp_salary, emp_department)

    hours_worked = int(input(f"Enter total hours worked for {emp_name}: "))
    e.calculate_emp_salary(hours_worked)

    employees.append(e)

for employee in employees:
    employee.print_employee_details()