name = input("Enter your name: ")
#Validating age
while True:
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Age is not an integer")
    else:
        break
#Validating phone_number
while True:    
    try:
        phone = int(input("Enter your phone: "))
    except ValueError:
        print("Phone is not an number")
    else:
        break
#Validating email
while True:
    email = input("Enter your email: ")
    if "@" or '.' not in email:
        print('Invalid Email')
    else:
        break
#Displaying user's profile
print("USER PROFILE:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Phone no: {phone}")
