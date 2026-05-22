import json
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
# Adding JSON profile
profile = {
    "name": name,
    "age": age,
    "email": email,
    "phone": phone
}
with open("profile.json", "w") as f:
    json.dump(profile, f, indent=4)
print("Profile saved to profile.json")
# Read and display saved profile
with open("profile.json", "r") as f:
    saved_profile = json.load(f)
print("\nSaved Profile:")
print(f"Name: {saved_profile['name']}")
print(f"Age: {saved_profile['age']}")
print(f"Email: {saved_profile['email']}")
print(f"Phone: {saved_profile['phone']}")