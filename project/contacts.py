import json

File_name = "contact.json"


def load_data():
    with open(File_name, "r") as file:
        return json.load(file)


def save_data(data):
    with open(File_name, "w") as file:
        json.dump(data, file, indent=4)


def add_contact(data):
    name = input("Enter the Name :: ")
    number = input("Enter the Contact Number :: ")

    new_contact = {
        "name": name,
        "phone": number
    }

    data["contacts"].append(new_contact)
    save_data(data)
    print("Contact Saved Successfully...")


def view_contact(data):
    
    for contact in data["contacts"]:
        print(f"Name : {contact['name']} \nPhone : {contact['phone']}")


def remove_contact(data):
    name = input("Enter the Name :: ")

    for contact in data["contacts"]:
        if contact["name"].lower() == name.lower():
            data["contacts"].remove(contact)
            save_data(data)
            print("Contact Removed")
            return

    print("Name Not Found")


def main():
    while True:
        data = load_data()

        print("1. Add Contacts")
        print("2. View Contact")
        print("3. Remove Contact")
        print("4. Exit")

        choice = int(input("Enter Your Choice :: "))

        if choice == 1:
            add_contact(data)

        elif choice == 2:
            view_contact(data)

        elif choice == 3:
            remove_contact(data)

        elif choice == 4:
            print("Program Exit....")
            exit()

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()