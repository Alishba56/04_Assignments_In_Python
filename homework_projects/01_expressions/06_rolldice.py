import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    total = die1 + die2
    
    print(f"Rolled: {die1} and {die2}")
    print(f"Total: {total}\n")

def main():
    roll_dice()

if __name__ == "__main__":
    main()
