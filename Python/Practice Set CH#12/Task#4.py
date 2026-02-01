try:
    a = int(input("Enter Number:"))
    b = int(input("Enter Number:"))
except ZeroDivisionError as z:
    print(z)

print(a/b)