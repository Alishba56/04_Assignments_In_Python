def main():
    feet = float(input("Enter the number of feet: "))
    inches = feet * 12
    print(f"{feet} foot{'s' if feet == 1 else 's'} is {inches} inches.")

if __name__ == "__main__":
    main()
