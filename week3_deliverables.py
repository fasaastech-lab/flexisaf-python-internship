# Categorise user by age group
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior")
# Define credentials
username = "fastmode"
password = "12345"
# Collect user login input
user_name = input("Enter your username: ")
pass_word = input("Enter your password: ")
# Validate credentials
if username == user_name and password == pass_word:
    print("Access granted")
else:
    print("Access Denied")
