class Contact:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter a name: ")
        email = input("Enter an Email: ")
        phnum = input("Enter a mobile number: ")
        address = input("Enter an Address: ")
        self.contacts[phnum] = {
            'name': name,
            'email': email,
            'address': address
        }
        print(f"Contact {name} saved successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for phnum, details in self.contacts.items():
                print(f"Name: {details['name']}, Phone Number: {phnum}, Email: {details['email']}, Address: {details['address']}")

    def search_contact(self):
        search1 = input("Enter name or mobile number to search: ")
        results = {phnum: details for phnum, details in self.contacts.items() if search1 in phnum or search1 in details['name']}
        if not results:
            print("Contact not found!")
        else:
            for phnum, details in results.items():
                print(f"Name: {details['name']}, Phone Number: {phnum}, Email: {details['email']}, Address: {details['address']}")

    def update_contact(self):
        phnum = input("Enter the mobile number of the contact to update: ")
        if phnum in self.contacts:
            name = input("Enter new name (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            if name:
                self.contacts[phnum]['name'] = name
            if email:
                self.contacts[phnum]['email'] = email
            if address:
                self.contacts[phnum]['address'] = address
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self):
        phnum = input("Enter the mobile number of the contact to delete: ")
        if phnum in self.contacts:
            del self.contacts[phnum]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def run(self):
        while True:
            print("\nContact Management System")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting Contact Management System.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = Contact()
    manager.run()
