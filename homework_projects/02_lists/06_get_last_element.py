def get_last_element(lst):
    print("The last element is:", lst[-1])

def main():
    n = int(input("How many elements in the list? "))

    user_list = []
    for i in range(n):
        item = input(f"Enter element {i + 1}: ")
        user_list.append(item)

    get_last_element(user_list)

if __name__ == "__main__":
    main()
