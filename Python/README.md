# 🐍 Python Learning Journey

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Learning-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

**A comprehensive repository documenting my Python programming journey**  
*Following CodeWithHarry's Ultimate Python Handbook*

[📚 Course Link](https://www.youtube.com/watch?v=UrsmFxEIp5k&t=4057s) • [📖 Handbook](./The_Ultimate_Python_Handbook_By_CodeWithHarry.pdf)

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Learning Path](#-learning-path)
- [Quick Notes](#-quick-notes)
- [Practice Sets](#-practice-sets)
- [Resources](#-resources)
- [Progress](#-progress)

---

## 🎯 About

This repository contains my complete Python learning experience following **CodeWithHarry's** YouTube tutorial series. Each chapter includes practice problems, notes, and hands-on projects to solidify understanding.

### Why Python?
- ✅ **Simple & Readable** - Feels like reading English
- ✅ **Versatile** - Web, AI, Data Science, Automation
- ✅ **High-Level Language** - Less code, more productivity
- ✅ **Open Source** - Free & community-driven
- ✅ **Cross-Platform** - Works on Linux, Windows, Mac

---

## 🗺️ Learning Path

### **Fundamentals** (Chapters 1-5)
```
📦 Basics
 ┣ 📂 CH#1 - Modules, Comments & pip
 ┣ 📂 CH#2 - Variables & Data Types
 ┣ 📂 CH#3 - Strings
 ┣ 📂 CH#4 - Lists & Tuples
 ┗ 📂 CH#5 - Dictionary & Sets
```

### **Control Flow** (Chapters 6-7)
```
🔄 Logic & Loops
 ┣ 📂 CH#6 - Conditional Expressions
 ┗ 📂 CH#7 - Loops in Python
```

### **Functions & I/O** (Chapters 8-9)
```
⚙️ Functions & Files
 ┣ 📂 CH#8 - Functions & Recursion
 ┗ 📂 CH#9 - File I/O
```

### **Object-Oriented Programming** (Chapters 10-11)
```
🎨 OOP Concepts
 ┣ 📂 CH#10 - OOP Basics
 ┗ 📂 CH#11 - Inheritance & Advanced OOP
```

### **Advanced Python** (Chapters 12-13)
```
🚀 Advanced Topics
 ┣ 📂 CH#12 - Advanced Python 1
 ┗ 📂 CH#13 - Advanced Python 2
```

---

## 📝 Quick Notes

### Chapter 1: Modules, Comments & pip
```python
# Installing external modules
pip install flask

# Single-line comment
# This is a comment

# Multi-line comment
"""
This is a
multi-line comment
"""
```

**Key Concepts:**
- **Modules**: Reusable code files (Built-in: `os`, `random` | External: `flask`, `tensorflow`)
- **pip**: Package manager for Python
- **REPL**: Interactive Python shell for quick testing

---

### Chapter 2: Variables & Data Types
```python
# Variable assignment
a = 30          # Integer
b = "harry"     # String
c = 71.22       # Float
d = True        # Boolean
e = None        # None type

# Type checking and conversion
type(a)         # <class 'int'>
str(31)         # "31"
int("32")       # 32
float(32)       # 32.0

# User input
name = input("Enter name: ")  # Always returns string
```

**Key Rules:**
- Variable names: letters, digits, underscores only
- Can't start with digits
- No whitespace allowed
- Case-sensitive

**Operators:**
- Arithmetic: `+`, `-`, `*`, `/`, `%`, `**`, `//`
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `and`, `or`, `not`
- Assignment: `=`, `+=`, `-=`, `*=`, `/=`

---

### Chapter 3: Strings
```python
# String creation
a = 'single quotes'
b = "double quotes"
c = '''triple quotes'''

# String slicing
word = "amazing"
word[0:3]      # "ama"
word[1:6:2]    # "mzn" (with step)
word[:7]       # "amazing" (start to 7)
word[-1]       # "g" (last character)

# String methods
str.len(word)              # 7
word.endswith("ing")       # True
word.count("a")            # 2
word.capitalize()          # "Amazing"
word.find("zi")            # 3
word.replace("a", "o")     # "omozing"

# Escape sequences
\n  # Newline
\t  # Tab
\\  # Backslash
\"  # Double quote
\'  # Single quote
```

---

### Chapter 4: Lists & Tuples
```python
# Lists (Mutable)
l1 = [1, 8, 7, 2, 21, 15]
l1[0]              # 1 (indexing)
l1[0:2]            # [1, 8] (slicing)
l1.sort()          # [1, 2, 7, 8, 15, 21]
l1.reverse()       # Reverse order
l1.append(8)       # Add to end
l1.insert(3, 8)    # Insert at index
l1.pop(2)          # Remove & return element
l1.remove(21)      # Remove specific value

# Tuples (Immutable)
a = (1, 7, 2)
a.count(1)         # Count occurrences
a.index(7)         # Find index
```

**List vs Tuple:**
| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | ✅ Yes | ❌ No |
| Speed | Slower | Faster |
| Use Case | Dynamic data | Fixed data |

---

### Chapter 5: Dictionary & Sets
```python
# Dictionary (Key-Value pairs)
a = {
    "name": "Harry",
    "from": "India",
    "marks": [92, 98, 96]
}
a["name"]              # "Harry"
a.keys()               # dict_keys(['name', 'from', 'marks'])
a.values()             # dict_values([...])
a.items()              # dict_items([...])
a.get("name")          # "Harry"
a.update({"age": 21})  # Add/update

# Sets (Unique, Unordered)
s = {1, 8, 2, 3}
s.add(5)               # Add element
s.remove(8)            # Remove element
s.union({8, 11})       # {1, 2, 3, 8, 11}
s.intersection({8, 1}) # {1}
```

**Properties:**
- Dictionary: Unordered, mutable, indexed, no duplicate keys
- Set: Unordered, unindexed, no duplicates

---

### Chapter 6: Conditional Expressions
```python
# If-elif-else
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

# Relational operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not

# Example
if (age >= 18) and (age <= 60):
    print("Working age")
```

---

### Chapter 7: Loops
```python
# While loop
i = 0
while i < 5:
    print(i)
    i += 1

# For loop
for item in [1, 2, 3]:
    print(item)

# Range function
for i in range(5):        # 0 to 4
    print(i)
    
for i in range(2, 7):     # 2 to 6
    print(i)
    
for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)

# Loop control
for i in range(10):
    if i == 3:
        break      # Exit loop
    if i == 5:
        continue   # Skip iteration
    print(i)
    
# For-else
for i in range(5):
    print(i)
else:
    print("Loop completed!")
```

---

### Chapter 8: Functions & Recursion
```python
# Function definition
def greet(name="stranger"):
    return f"Hello, {name}!"

# Function call
message = greet("Harry")  # "Hello, Harry!"
message = greet()         # "Hello, stranger!"

# Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

factorial(5)  # 120
```

**Types:**
- Built-in: `len()`, `print()`, `range()`
- User-defined: Custom functions

---

### Chapter 9: File I/O
```python
# Reading files
f = open("file.txt", "r")
content = f.read()
f.close()

# Writing files
f = open("file.txt", "w")
f.write("Hello World")
f.close()

# With statement (Auto-close)
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

# File modes
# 'r' - Read (default)
# 'w' - Write (overwrites)
# 'a' - Append
# 'r+' - Read & Write
# 'rb' - Read binary
```

---

### Chapter 10: Object-Oriented Programming
```python
# Class & Object
class Employee:
    company = "Google"  # Class attribute
    
    def __init__(self, name, salary):
        self.name = name        # Instance attribute
        self.salary = salary
    
    def getSalary(self):
        return f"{self.name}: ${self.salary}"
    
    @staticmethod
    def greet():
        print("Hello!")

# Object creation
harry = Employee("Harry", 50000)
print(harry.getSalary())  # "Harry: $50000"
Employee.greet()          # "Hello!"
```

**Key Concepts:**
- **Class**: Blueprint for objects
- **Object**: Instance of a class
- **`__init__`**: Constructor method
- **self**: Reference to instance
- **@staticmethod**: Method without self

---

### Chapter 11: Inheritance & Advanced OOP
```python
# Inheritance
class Employee:
    def __init__(self, name):
        self.name = name

class Programmer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

# Multiple Inheritance
class A:
    pass

class B:
    pass

class C(A, B):
    pass

# Property decorator
class Employee:
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        self._salary = value

# Operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

**Types of Inheritance:**
- Single: `class B(A)`
- Multiple: `class C(A, B)`
- Multilevel: `class C(B)` where `class B(A)`

---

### Chapter 12: Advanced Python 1
```python
# Walrus operator (Python 3.8+)
if (n := len([1, 2, 3])) > 2:
    print(f"Length is {n}")

# Type hints
def greeting(name: str) -> str:
    return f"Hello, {name}"

# Match-case (Python 3.10+)
status = 200
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Unknown")

# Exception handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"General error: {e}")
else:
    print("Success!")
finally:
    print("Cleanup")

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Enumerate
for i, item in enumerate(['a', 'b', 'c']):
    print(i, item)
```

---

### Chapter 13: Advanced Python 2
```python
# Virtual environment
# python -m venv myenv
# source myenv/bin/activate  (Linux/Mac)
# myenv\Scripts\activate     (Windows)

# Lambda functions
square = lambda x: x**2
add = lambda a, b: a + b

# Map, Filter, Reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)

# String methods
words = ["apple", "banana", "cherry"]
result = ", ".join(words)  # "apple, banana, cherry"

# Format method
msg = "{} is {} years old".format("Harry", 25)
msg = "{name} is {age} years old".format(name="Harry", age=25)
```

---

## 🎯 Practice Sets

Each chapter includes practice problems to reinforce learning:

- **Chapter 1**: Modules & Comments exercises
- **Chapter 2**: Variables & operators problems
- **Chapter 3**: String manipulation tasks
- **Chapter 4**: List & tuple operations
- **Chapter 5**: Dictionary & set challenges
- **Chapter 6**: Conditional logic problems
- **Chapter 7**: Loop practice exercises
- **Chapter 8**: Function & recursion tasks
- **Chapter 9**: File handling projects
- **Chapter 10**: OOP basic exercises
- **Chapter 11**: Inheritance challenges
- **Chapter 12**: Advanced Python 1 tasks
- **Chapter 13**: Advanced Python 2 problems

---

## 📚 Resources

### Official Documentation
- [Python Official Docs](https://docs.python.org/3/)
- [Python Package Index (PyPI)](https://pypi.org/)

### Learning Resources
- [CodeWithHarry YouTube Channel](https://www.youtube.com/@CodeWithHarry)
- [Ultimate Python Handbook](./The_Ultimate_Python_Handbook_By_CodeWithHarry.pdf)

### Tools & Libraries
- [pip Documentation](https://pip.pypa.io/)
- [virtualenv](https://virtualenv.pypa.io/)
- [Flask](https://flask.palletsprojects.com/)

---

## 📈 Progress

### Completed ✅
- [x] Chapter 1 - Modules, Comments & pip
- [x] Chapter 2 - Variables & Data Types
- [x] Chapter 3 - Strings
- [x] Chapter 4 - Lists & Tuples
- [x] Chapter 5 - Dictionary & Sets
- [x] Chapter 6 - Conditional Expressions
- [x] Chapter 7 - Loops
- [x] Chapter 8 - Functions & Recursion
- [x] Chapter 9 - File I/O
- [x] Chapter 10 - OOP Basics
- [x] Chapter 11 - Inheritance & Advanced OOP
- [x] Chapter 12 - Advanced Python 1
- [x] Chapter 13 - Advanced Python 2

## 🤝 Contributing

Feel free to fork this repository and add your own solutions or improvements!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- **CodeWithHarry** - For the excellent Python tutorial series
- **Python Community** - For maintaining comprehensive documentation

---

<div align="center">

### 💡 Keep Learning, Keep Coding!

Made by [Syed-Hasham](https://github.com/Syed-Hasham)

⭐ Star this repo if you found it helpful!

</div>
