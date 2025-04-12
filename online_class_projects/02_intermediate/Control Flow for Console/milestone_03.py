import random

def main():
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"User's number: {user_number}")
    print(f"Computer's number: {computer_number}")

    while True:
        guess = input("Do you think your number is 'higher' or 'lower' than the computer's? ").strip().lower()
        if guess in ["higher", "lower"]:
            break
        print("Invalid input. Please type 'higher' or 'lower'.")

    if user_number == computer_number:
        print("It's a tie, but the computer wins by default!")
    elif guess == "higher" and user_number > computer_number:
        print("You win! Your number is higher.")
    elif guess == "lower" and user_number < computer_number:
        print("You win! Your number is lower.")
    else:
        print("You lose!")

if __name__ == "__main__":
    main()
