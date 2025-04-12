import random

NUM_ROUNDS = 5
def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    score = 0
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"--- Round {round_num} ---")

        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number: {user_number}")

        while True:
            guess = input("Do you think your number is 'higher' or 'lower' than the computer's? ").strip().lower()
            if guess in ['higher', 'lower']:
                break
            print("Invalid input. Please type 'higher' or 'lower'.")

        if user_number == computer_number:
            print("It's a tie, but the computer wins by default!")
        elif guess == "higher" and user_number > computer_number:
            print("You win! Your number is higher.")
            score += 1
        elif guess == "lower" and user_number < computer_number:
            print("You win! Your number is lower.")
            score += 1
        else:
            print("You lose!")

        print(f"Your score: {score}\n")

    print("Game over!")
    print(f"Final score: {score} out of {NUM_ROUNDS}")

if __name__ == "__main__":
    main()
