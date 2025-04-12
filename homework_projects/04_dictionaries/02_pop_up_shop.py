def main():
    fruit_prices = {
        "apple": 3.5,
        "durian": 15.0,
        "jackfruit": 18.0,
        "kiwi": 2.5,
        "rambutan": 8.5,
        "mango": 10.0
    }

    total = 0.0

    for fruit, price in fruit_prices.items():
        quantity_input = input(f"How many ({fruit}) do you want?: ").strip()
        try:
            quantity = int(quantity_input)
            total += quantity * price
        except ValueError:
            print(f"Invalid input for {fruit}. Assuming 0.")

    print(f"Your total is ${total:.2f}")

if __name__ == "__main__":
    main()
