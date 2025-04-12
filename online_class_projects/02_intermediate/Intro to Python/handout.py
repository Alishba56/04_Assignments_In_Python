def main():
    earth_weight = float(input("Enter your weight on Earth (in kg): "))
    mars_weight = earth_weight * 0.378
    mars_weight = round(mars_weight, 2)
    print(f"Your weight on Mars would be {mars_weight} kg.")

if __name__ == "__main__":
    main()
