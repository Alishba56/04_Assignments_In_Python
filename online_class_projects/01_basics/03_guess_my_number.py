import random

def guess_my_number():
    number_to_guess = random.randint(0, 99)
    while True:
        guess = int(input("Enter a guess: "))
        if guess > number_to_guess:
            print("Your guess is too high")
        elif guess < number_to_guess:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {number_to_guess}")
            break

def main():
    print("Welcome to the Number Guessing Game!")
    guess_my_number()

if __name__ == "__main__":
    main()
