import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    try:
        num_passwords = int(input("How many passwords do you want to generate?: "))
        length = int(input("What length should each password be?: "))

        print("\nHere are your passwords:")
        for _ in range(num_passwords):
            print(generate_password(length))
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
