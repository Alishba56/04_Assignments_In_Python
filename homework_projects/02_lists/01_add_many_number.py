def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
def main():
    my_list = [ 10, 50,20, 30, 40]
    
    result = sum_of_numbers(my_list)
    
    print(f"The sum is: {result}")

if __name__ == "__main__":
    main()
