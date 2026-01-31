print("Multiple Inheritance")

class Employee:
    company = "ITC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Coder:
    def __init__(self, language):
        self.language = language

    def showLanguage(self):
        print(f"He is good with {self.language} language")

class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def __init__(self, name, salary, language):
        Employee.__init__(self, name, salary)
        Coder.__init__(self, language)

a = Employee("ABC", 100)
b = Programmer("XYZ", 200, "Python")

b.show()
b.showLanguage()
