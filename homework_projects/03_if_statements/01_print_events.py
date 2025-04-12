def print_even_numbers(count):
    for i in range(count):
        even_number = i * 2
        print(even_number, end=' ')

def main():
    count = 20
    print("The first 20 even numbers are:")
    print_even_numbers(count)

if __name__ == "__main__":
    main()
