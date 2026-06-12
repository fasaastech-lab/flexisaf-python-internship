# Get password input
password = input("Enter password: ")

# Check password length
if len(password) >= 12:
    print("Your password length is strong")
elif len(password) >= 8:
    print("Your password length is medium")
else:
    print("Your password length is weak")

# Set flag for numbers and special characters in password
has_number = False
has_special = False
special = ['!','@','#','$','%','&','*','~','|','/']

# Verify number and special characters in password
for char in password:
    if char.isdigit():
        has_number = True
    if char in special:
        has_special = True