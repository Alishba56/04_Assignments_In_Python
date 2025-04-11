age = int(input("How old are you? "))

voting_ages = {
    "Peturksbouipo": 16,
    "Stanlau": 25,
    "Mayengua": 48
}

for country, required_age in voting_ages.items():
    if age >= required_age:
        print(f"You can vote in {country} where the voting age is {required_age}.")
    else:
        print(f"You cannot vote in {country} where the voting age is {required_age}.")
21