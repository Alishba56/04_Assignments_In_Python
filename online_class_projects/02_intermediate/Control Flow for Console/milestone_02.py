import random

def main():
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"User's number: {user_number}")
    print(f"Computer's number: {computer_number}")

    guess = input("Do you think your number is 'higher' or 'lower' than the computer's? ").strip().lower()

    print(f"You guessed: {guess}")

if __name__ == "__main__":
    main()

