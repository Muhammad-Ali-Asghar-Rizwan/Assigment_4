# Project 6: Countdown Timer Python Project



import time
def countdown_timer(seconds):
    print("Countdown Timer")
    print("Time remaining:")
    
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!")


if __name__ == "__main__":
    try:
        total_seconds = int(input("Enter the time in seconds: "))
        countdown_timer(total_seconds)
    except ValueError:
        print("Please enter a valid number of seconds.")    