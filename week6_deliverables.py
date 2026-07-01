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
        id = input("Enter an ID: ")
        if id in contacts:
            print("This ID is already taken")
        else:
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            phone = input("Enter your phone number: ")
            role = input("Enter your role: ")
            if email in used_emails:
                print("This email is already taken")
            elif phone in used_phones:
                print("This phone number is already taken")
            else:
                contacts[id] = {"name": name, "email": email, "phone": phone, "role": role}
                used_emails.add(email)
                used_phones.add(phone)
                print("Contact added successfully")
    elif choice == "2":
        if not contacts:
            print("Contacts is empty")
        else:
            for id, info in contacts.items():
                print(f"\nID: {id}")
                print(f"Name: {info["name"]}")
                print(f"Email: {info["email"]}")
                print(f"Phone: {info["phone"]}")
                print(f"Role: {info["role"]}")
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        break