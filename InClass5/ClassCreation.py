class Employee(object):
    countEmployees = 0

    def __init__(self):
        self.name = "Madhuri"
        self.salary = 50000


    def countOfEmployees(self):
        Employee.countEmployees = Employee.countEmployees + 1
        print("No. of employees:%d" %(Employee.countEmployees))


    def displayEmployeeDetails(self,name,salary):
        print("Name:" + name + '\n')
        print("Salary:" + salary)

class Manager(Employee):
    def __init__(self):
        super(Manager,self).__init__()
        self.salary = 30000
        self.name = "Madhuri Gumma"


print("Enter Name and salary:")
name = input()
salary = input()
emp1 = Manager()
emp1.countOfEmployees()
emp1.displayEmployeeDetails(name,salary)

print("Enter another Name and salary:")
name1 = input()
salary1 = input()
emp2 = Manager()
emp2.countOfEmployees()
emp2.displayEmployeeDetails(name1,salary1)