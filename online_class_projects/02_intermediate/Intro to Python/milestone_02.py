def main():
    gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.360,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.140
    }

    earth_weight = float(input("Enter your weight on Earth (in pounds or kg): "))
    planet = input("Enter the name of a planet: ")

    if planet in gravity:
        planet_weight = earth_weight * gravity[planet]
        print(f"Your weight on {planet} would be {planet_weight:.2f}.")
    else:
        print("That planet is not in our list.")

if __name__ == "__main__":
    main()
