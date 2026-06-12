# Get password input
password = input("Enter password: ")

# Check password length
if len(password) >= 12:
    print("Your password length is strong")
elif len(password) >= 8:
    print("Your password length is medium")
else:
    print("Your password length is weak")

