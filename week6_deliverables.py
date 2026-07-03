# Initialize contacts dictionary and sets to track unique emails and phones
contacts = {}
used_emails = set()
used_phones = set()

# Main menu loop
while True:
    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")
    choice = input("Choose an option: ")

    # Add new contact with duplicate checks
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

    # Display all contacts
    elif choice == "2":
        if not contacts:
            print("Contacts is empty")
        else:
            for id, info in contacts.items():
                print(f"\nID: {id}")
                print(f"Name: {info['name']}")
                print(f"Email: {info['email']}")
                print(f"Phone: {info['phone']}")
                print(f"Role: {info['role']}")

    # Search contact by ID
    elif choice == "3":
        id = input("Enter contact ID: ")
        if id in contacts:
            info = contacts[id]
            print(f"\nName: {info['name']}")
            print(f"Email: {info['email']}")
            print(f"Phone: {info['phone']}")
            print(f"Role: {info['role']}")
        else:
            print("Contact not found.")

    # Update a specific field of an existing contact
    elif choice == "4":
        id = input("Enter contact ID: ")
        if id not in contacts:
            print("ID doesn't exist")
        else:
            field = input("Enter field to update (name, email, phone, role): ")
            if field.lower() == "name":
                new_name = input("Enter new name: ")
                contacts[id]["name"] = new_name
                print("Name updated successfully")
            elif field.lower() == "email":
                new_email = input("Enter new email: ")
                if new_email in used_emails:
                    print("Email already taken")
                else:
                    used_emails.remove(contacts[id]["email"])
                    used_emails.add(new_email)
                    contacts[id]["email"] = new_email
                    print("Email updated successfully")
            elif field.lower() == "phone":
                new_phone = input("Enter new phone: ")
                if new_phone in used_phones:
                    print("Phone already taken")
                else:
                    used_phones.remove(contacts[id]["phone"])
                    used_phones.add(new_phone)
                    contacts[id]["phone"] = new_phone
                    print("Phone updated successfully")
            elif field.lower() == "role":
                new_role = input("Enter new role: ")
                contacts[id]["role"] = new_role
                print("Role updated successfully")
            else:
                print("Invalid field. Choose name, email, phone, or role")

    # Delete contact and remove from tracking sets
    elif choice == "5":
        id = input("Enter ID to delete: ")
        if id in contacts:
            used_emails.remove(contacts[id]["email"])
            used_phones.remove(contacts[id]["phone"])
            del contacts[id]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    # Exit the program
    elif choice == "6":
        break

    # Handle invalid menu choices
    else:
        print("Invalid option. Please choose between 1 and 6.")