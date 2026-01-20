import os

# Get and print contents of the current directory
contents = os.listdir('.')
print("Contents of the current directory:")
for item in contents:
    print(item)