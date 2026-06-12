# Get password input
password = input("Enter password: ")

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

# Check password strength
if len(password) >= 12 and has_number and has_special:
    print("Password is strong")
    print("Tip: Great password!") 
elif len(password) >= 8 and (has_special or has_number):
    print("Password is medium")
    print("Tip: Add special characters and " 
        "increase length to 12+ for a stronger password.")
else:
    print("Password length is weak")
    print("Tip: Use at least 8 characters," 
        "include numbers and special characters like !@#$.")