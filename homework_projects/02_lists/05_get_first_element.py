def get_first_element(lst):
    print("The first element is:", lst[0])

def main():
    n = int(input("How many elements in the list? "))
    
    user_list = []
    for i in range(n):
        item = input(f"Enter element {i + 1}: ")
        user_list.append(item)

    get_first_element(user_list)

if __name__ == "__main__":
    main()
