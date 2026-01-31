print("Multilevel Inheritance")

class Employee:
    company = "ITC"

    def __init__(self, name):
        self.name = name

    def showName(self):
        print(f"Employee Name: {self.name}")

class Programmer(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def showSalary(self):
        print(f"Salary: {self.salary}")

class SeniorProgrammer(Programmer):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def showLanguage(self):
        print(f"Expert in: {self.language}")

# Object of the last class
sp = SeniorProgrammer("XYZ", 50000, "Python")

sp.showName()
sp.showSalary()
sp.showLanguage()
