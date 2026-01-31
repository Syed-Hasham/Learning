class Employee:
    a=1
    @classmethod #used to bound to the class rather than the object
    def show(cls):
        print(f"The class value of a is {cls.a}")
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ") [1]

e = Employee()
e.a=45
e.name="XYZ ABC"
print(e.fname,e.lname)
e.show()