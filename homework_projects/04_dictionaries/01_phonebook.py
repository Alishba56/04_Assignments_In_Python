def main():
    phonebook = {}

    while True:
        action = input("Type 'add' to add a contact, 'lookup' to find a contact, or press Enter to quit: ").strip().lower()

        if action == "":
            break
        elif action == "add":
            name = input("Enter name: ").strip()
            number = input("Enter phone number: ").strip()
            phonebook[name] = number
            print(f"Added {name} to phonebook.")
        elif action == "lookup":
            name = input("Enter name to look up: ").strip()
            if name in phonebook:
                print(f"{name}'s number is {phonebook[name]}")
            else:
                print(f"{name} is not in the phonebook.")
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
