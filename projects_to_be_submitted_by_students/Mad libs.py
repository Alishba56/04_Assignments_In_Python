def main():
    print("Welcome to Mad Libs!")

    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    story = f"Today, I saw a {adjective} {noun} that decided to {verb} {adverb} down the street!"
    
    print("\nHere's your Mad Libs story:")
    print(story)

main()
