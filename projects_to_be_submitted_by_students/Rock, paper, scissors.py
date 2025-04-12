import random

def play_rps():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in options:
        print("That's not a valid choice.")
        return

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

def main():
    while True:
        play_rps()
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
