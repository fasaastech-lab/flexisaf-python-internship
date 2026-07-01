contacts = {}
used_emails = set()
used_phones = set()

while True:
    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        id = input("Enter a ID: ")
        if id in contacts:
            print("This ID has been taken")
        else:
            name = input("Enter your name: ")
            email = input("Enter your email")
            phone = input("Enter your phone number: ")
            role = input("Enter your role: ")
        contacts[id] = {"name": name, "email": email, "phone": phone, "role": role}
        if email in used_emails:
            print("This email is taken. Pick another one")
        else:
            used_emails.add(email)
        if phone in used_phones:
            print("This phone number is taken. Pick another one") 
        else:
            used_phones.add(phone)
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        break