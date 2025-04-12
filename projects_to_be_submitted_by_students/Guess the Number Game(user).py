import random

def computer_guesses_number():
    print("Think of a number between 1 and 100 and I will try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while True:
        if low > high:
            print("Hmm... something doesn't add up. Are you sure you're answering correctly?")
            break

        guess = random.randint(low, high)
        attempts += 1
        print(f"My guess is: {guess}")

        feedback = input("Is it too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Yay! I guessed your number in {attempts} tries!")
            break
        else:
            print("Please respond with H, L, or C.")

def main():
    computer_guesses_number()

if __name__ == "__main__":
    main()
