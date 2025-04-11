MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print("Removed:", removed_item)

def main():
    items = []
    num_items = int(input("How many items in the list? "))
    for i in range(num_items):
        item = input(f"Enter item {i + 1}: ")
        items.append(item)

    print("Original list:", items)
    shorten(items)
    print("Shortened list:", items)

if __name__ == "__main__":
    main()
