import os

# Get the directory where the script is being run
current_dir = os.getcwd()
print(f"Creating files in: {current_dir}")

for n in range(1, 6):
    filename = f"Task#{n}.py"
    filepath = os.path.join(current_dir, filename)

    with open(filepath, "w") as f:
        f.write(f"")

    print(f"Created {filepath}")
