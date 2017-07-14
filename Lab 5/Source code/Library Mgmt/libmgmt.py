class Person(object):
    countEmployees = 0

    def __init__(self):
        self.name = "Madhuri"
        self.salary = 50000


    def countOfEmployees(self):
        Person.countEmployees = Person.countEmployees + 1
        print("No. of employees:%d" %(Person.countEmployees))


    def displayEmployeeDetails(self,name):
        print("Name:" + name + '\n')


class book(object):
    isAvailable = "true"
    def __init__(self,name,author):
        self.title = name
        self.author = author
    def isAvailable(self,isAvailable):
            return isAvailable


class Librarian(Person):

    def __init__(self):
        super(Librarian,self).__init__()
        self.name = "Madhuri Gumma"
    def experience(self,years):
        print("Experience as librarian:%d"  %(years))

class Student(Person):
    def __init__(self):
        super(Student,self).__init__()
        self.name = "Kranthi"
    def majorDisplay(self,major):
        print("Major Enrolled:" + major)
    def booksIssued(self,numBooks):
        print("No. of books issued:%d" %(numBooks))

class Staff(Person):
    def __init__(self):
        super(Student,self).__init__()
        self.name = "Madhuri Gumma"
        self.salary = 60000

print("Enter Name of the Librarian:")
name = input()
emp1 = Librarian()
emp1.experience(5)
emp1.countOfEmployees()
emp1.displayEmployeeDetails(name)

print("Enter Name and major of student:")
name1 = input()
major = input()
student = Student()
student.majorDisplay(major)
student.booksIssued(3)

print("\nEnter name and author of the book:")
bookName1 = input()
author = input()
book1 = book(bookName1,author)
available = book1.isAvailable("available")
print(available)