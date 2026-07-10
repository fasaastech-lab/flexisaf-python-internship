import os

# Get source and destination file names from user
source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

try:
    # Check if source file exists
    with open(source, "r") as src:
        content = src.read()

    # Check if destination file already exists to prevent overwrite
    if os.path.exists(destination):
        confirm = input(f"{destination} already exists. Overwrite? (yes/no): ")
        if confirm.lower() != "yes":
            print("Copy cancelled.")
        else:
            with open(destination, "w") as dst:
                dst.write(content)
            print(f"File copied from {source} to {destination} successfully.")
    else:
        # Write content to destination file
        with open(destination, "w") as dst:
            dst.write(content)
        print(f"File copied from {source} to {destination} successfully.")

except FileNotFoundError:
    # Handle missing source file
    print(f"Error: '{source}' not found. Please check the file name.")

except PermissionError:
    # Handle permission issues
    print("Error: Permission denied. Cannot read or write file.")

except Exception as e:
    # Handle any other unexpected error
    print(f"Unexpected error: {e}")