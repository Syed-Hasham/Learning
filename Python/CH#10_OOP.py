#class initiation
class employee:
    #Class Attributes
    language = "R"
    salary = 99999999999
    
    #Methods
    def getinfo(self):
        print(f"\nLanguage: {self.language}\nSalary:{self.salary}")
    
    @staticmethod #Doesn't require self parameter
    def greet():
        print("\n Hello!")

abc = employee()
print("\n",abc.language ,abc.salary)

efg = employee()
efg.name="EFG" #Instance Attribute
print("\n",efg.language,efg.salary)

hij = employee()
hij.language="PY"
print("\n",hij.language,hij.salary)

#Hij.language will be "PY" instead of R
#Instance Attributes Take Priority Over Class Attributes

hij.getinfo()
hij.greet()



#Constructors
class employee2:
    language = "R"
    salary = 99999999999
    
    def getinfo(self):
        print(f"Language: {self.language}\nSalary:{self.salary}")
    
    def __init__(self,language,salary): #Automatically runs when object is created
        self.language = language
        self.salary = salary
        print("\nObj Created")

klm = employee2("JS",100)
klm.getinfo()