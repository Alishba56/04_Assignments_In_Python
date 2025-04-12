def print_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    print(f"Here are the divisors of {num}:")
    print(" ".join(map(str, divisors)))

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

if __name__ == "__main__":
    main()
