# Validating name
while True:
    name = input("Enter your name: ")
    if not name.strip():
        print("Name cannot be empty")
    else:
        break
# Validating age
while True:
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Age is not an integer")
    else:
        break
# Validating email
while True:
    email = input("Enter your email: ")
    if "@" not in email or "." not in email:
        print("Invalid Email")
    else:
        break
# Validating phone_number
while True:
    phone = input("Enter your phone: ")
    if not phone.isdigit():
        print("Phone must contain numbers only")
    else:
        break
# Displaying user's profile
print("USER PROFILE:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Phone no: {phone}")
