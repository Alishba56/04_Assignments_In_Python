def even_odd_sequence():
    for num in range(10, 20):
        if num % 2 == 0:
            print(f"{num} even", end=" ")
        else:
            print(f"{num} odd", end=" ")

even_odd_sequence()
