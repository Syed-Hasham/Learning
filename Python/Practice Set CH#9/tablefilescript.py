import os

# Get the directory where the script is being run
current_dir = os.getcwd()
print(f"Creating files in: {current_dir}")

for n in range(1, 21):
    filename = f"table_{n}.txt"
    filepath = os.path.join(current_dir, filename)

    # Create empty file
    with open(filepath, "w"):
        pass

    print(f"Created {filepath}")
