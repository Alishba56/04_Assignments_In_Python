import random

def get_random_word():
    word_list = ["python", "hangman", "challenge", "developer", "program"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = get_random_word()
    guessed_letters = set()
    tries = 6

    print("Welcome to Hangman!")
    
    while tries > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            print("Correct!")
            guessed_letters.add(guess)
        else:
            print("Wrong!")
            guessed_letters.add(guess)
            tries -= 1

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nYou ran out of tries. The word was: {word}")

def main():
    hangman()

if __name__ == "__main__":
    main()
