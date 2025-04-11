import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print("Rolled:", die1, "and", die2)

def main():
    print("Rolling two dice three times...\n")
    
    roll_dice()
    roll_dice()
    roll_dice()
    roll_dice()
    roll_dice()
    roll_dice()

if __name__ == "__main__":
    main()
