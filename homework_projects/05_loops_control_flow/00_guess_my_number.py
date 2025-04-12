import random

def guess_my_number():
    number_to_guess = random.randint(0, 99)
    while True:
        try:
            guess = int(input("Enter a guess: "))
            if guess > number_to_guess:
                print("Your guess is too high")
            elif guess < number_to_guess:
                print("Your guess is too low")
            else:
                print(f"Congrats! The number was: {number_to_guess}")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guess_my_number()
