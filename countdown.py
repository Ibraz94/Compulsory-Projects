import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def main():
    try:
        duration = int(input("Enter the countdown duration in seconds: "))
        if duration < 0:
            print("Please enter a positive number.")
            return
        countdown(duration)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
