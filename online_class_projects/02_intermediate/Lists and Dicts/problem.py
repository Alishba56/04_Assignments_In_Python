def access_element(my_list, index):
    try:
        return f"Element at index {index} is: {my_list[index]}"
    except IndexError:
        return "Index out of range!"

def modify_element(my_list, index, new_value):
    try:
        old_value = my_list[index]
        my_list[index] = new_value
        return f"Replaced '{old_value}' with '{new_value}' at index {index}."
    except IndexError:
        return "Index out of range!"

def slice_list(my_list, start, end):
    try:
        sliced = my_list[start:end]
        return f"Sliced list from index {start} to {end}: {sliced}"
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print("Welcome to the Index Game!")
    print(f"Current list: {my_list}")

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            index = int(input("Enter the index you want to access: "))
            print(access_element(my_list, index))

        elif choice == '2':
            index = int(input("Enter the index you want to modify: "))
            new_value = input("Enter the new value: ")
            print(modify_element(my_list, index, new_value))
            print(f"Updated list: {my_list}")

        elif choice == '3':
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            print(slice_list(my_list, start, end))

        elif choice == '4':
            print("Thanks for playing the Index Game!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
