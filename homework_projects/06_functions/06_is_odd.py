def even_odd_sequence():
    for num in range(10, 20):
        if num % 2 == 0:
            print(f"{num} even", end=" ")
        else:
            print(f"{num} odd", end=" ")
    print()  # Add newline after the loop for clean output

def main():
    even_odd_sequence()

if __name__ == "__main__":
    main()
