def subtract_seven(num):
    return num - 7

def main():
    num = int(input("Enter a number: "))
    
    result = subtract_seven(num)
    
    print(f"Result after subtracting 7: {result}")

if __name__ == "__main__":
    main()
