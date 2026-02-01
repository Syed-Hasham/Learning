#Walrus Operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
#n=5

#Type Definitions
a : int = 5
name : str = "ABC"

def sum(b : int , c : int) -> int:
    return b+c

from typing import List, Tuple, Dict, Union
numbers: List[int] = [1, 2, 3, 4, 5]
person: Tuple[str, int] = ("Alice", 30)
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
identifier: Union[int, str] = "ID123"
identifier = 12345 

#easier to document code

#Match Case i.e switch case 
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"
# Usage
print(http_status(200)) # Output: OK
print(http_status(404)) # Output: Not Found
print(http_status(500)) # Output: Internal Server Error
print(http_status(403)) # Output: Unknown status

#Exception Handling
try:
    f = int (input("Enter A Number: "))
    print(f)
except ValueError as e:
    print(e)
else:
    print("Continue.")
# raise ValueError("Valid Integer Will Be Accepted")
# finally:
    # Some Code
    # Executed regardless of error!

#Enumerate Function
list1 = [1,7,12,11,22]
for i,item in enumerate(list1):
    print(i,item) # Prints the items of list 1 with index
#LIST COMPREHENSIONS
list2 = [item for item in list1 if item > 8]
#OUTPUT : [12,11,22]
print(list2)