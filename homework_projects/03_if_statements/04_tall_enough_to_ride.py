MIN_HEIGHT = 50

def check_height():
    height = int(input("How tall are you? "))

    if height >= MIN_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    check_height()
