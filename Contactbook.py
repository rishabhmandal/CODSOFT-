def display_menu():
    print("\nContact Book Menu")
    print("1. Add Contact"),
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact '{name}' added.")


def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\nContacts List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}")


def search_contact(contacts):
    search = input("Enter name or phone number to search: ")
    for name, info in contacts.items():
        if search in (name, info['phone']):
            print(
                f"\nFound contact - Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")
            return
    print(f"No contact found for '{search}'.")


def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Updating contact for '{name}'")
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"Contact '{name}' updated.")
    else:
        print(f"No contact found for '{name}'.")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"No contact found for '{name}'.")


def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
