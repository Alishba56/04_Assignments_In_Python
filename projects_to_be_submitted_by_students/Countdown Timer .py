import time

def countdown(seconds):
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        time_format = f"{mins:02d}:{secs:02d}"
        print(time_format, end='\r')  # Print on the same line
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def main():
    try:
        total_seconds = int(input("Enter countdown time in seconds: "))
        countdown(total_seconds)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
