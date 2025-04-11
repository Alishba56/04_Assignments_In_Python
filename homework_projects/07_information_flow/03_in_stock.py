def num_in_stock(fruit):
    inventory = {
        "apple": 50,
        "banana": 30,
        "pear": 1000,
        "orange": 200,
        "mango": 0
    }
    
    return inventory.get(fruit, 0)

def main():
    fruit = input("Enter a fruit: ").lower()  
    stock = num_in_stock(fruit)
    
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

main()
