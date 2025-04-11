def double_list(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2
    return numbers

def main():
    numbers = [1, 2, 3, 4]
    print("Original list:", numbers)

    doubled = double_list(numbers)
    print("Doubled list:", doubled)

if __name__ == "__main__":
    main()
