def print_multiple(message, repeats):
    for _ in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")

    while True:
        try:
            repeats = int(input("Enter a number of times to repeat your message: "))
            break  
        except ValueError:
            print("Please enter a valid number.")

    print_multiple(message, repeats)

main()
