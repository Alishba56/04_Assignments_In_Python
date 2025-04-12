import random

def play_round():
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"\nYour number: {user_number}")

    while True:
        guess = input("Do you think your number is 'higher' or 'lower' than the computer's? ").strip().lower()
        if guess in ["higher", "lower"]:
            break
        print("Invalid input. Please type 'higher' or 'lower'.")

    print(f"Computer's number: {computer_number}")

    if user_number == computer_number:
        print("It's a tie! The computer wins by default.")
        return 0
    elif guess == "higher" and user_number > computer_number:
        print("You win! Your number is higher.")
        return 1
    elif guess == "lower" and user_number < computer_number:
        print("You win! Your number is lower.")
        return 1
    else:
        print("You lose!")
        return 0

def main():
    print("Welcome to the High-Low Game!")

    while True:
        rounds_input = input("How many rounds would you like to play? ")
        if rounds_input.isdigit():
            rounds = int(rounds_input)
            break
        else:
            print("Please enter a valid number.")

    score = 0
    for _ in range(rounds):
        score += play_round()

    print(f"\nGame over! You scored {score} out of {rounds}.")

if __name__ == "__main__":
    main()
