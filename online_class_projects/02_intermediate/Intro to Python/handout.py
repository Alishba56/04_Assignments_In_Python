def main():
    # Prompt the user for their Earth weight
    earth_weight = float(input("Enter your weight on Earth (in kg): "))

    # Calculate weight on Mars
    mars_weight = earth_weight * 0.378

    # Round to two decimal places
    mars_weight = round(mars_weight, 2)

    # Print the result
    print(f"Your weight on Mars would be {mars_weight} kg.")

# Call the main function
if __name__ == "__main__":
    main()
