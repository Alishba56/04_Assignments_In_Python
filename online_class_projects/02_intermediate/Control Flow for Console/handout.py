import random

def play_round():
    user_num = random.randint(1, 100)
    computer_num = random.randint(1, 100)

    print(f"\nYour number is: {user_num}")
    guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()

    if guess not in ['higher', 'lower']:
        print("Invalid guess. You lose this round.")
        return 0

    print(f"The computer's number was: {computer_num}")

    if (guess == "higher" and user_num > computer_num) or (guess == "lower" and user_num < computer_num):
        print("Correct guess! You get a point.")
        return 1
    else:
        print("Wrong guess. No point for you.")
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
