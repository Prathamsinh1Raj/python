import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()

    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = phone
        save_contacts(contacts)
        print("Contact added successfully.")

def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter name to update: ").strip()
    if name in contacts:
        new_phone = input("Enter new phone number: ").strip()
        contacts[name] = new_phone
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
