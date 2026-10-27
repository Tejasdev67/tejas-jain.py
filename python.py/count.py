import time

def start_countdown():
    print("====================================")
    print("         Countdown Timer            ")
    print("====================================")

    user_input = input("Enter the countdown time in seconds: ").strip()

    if not user_input.isdigit():
        print("❌ Invalid input! Please enter a whole number of seconds.")
        return

    seconds = int(user_input)

    print("\nTimer started!")
    while seconds > 0:
        # Calculate minutes and remaining seconds
        mins, secs = divmod(seconds, 60)
        
        # Format the time as MM:SS string
        timer_display = f"{mins:02d}:{secs:02d}"
        
        # Print the time over writing the line using carriage return (\r)
        print(timer_display, end="\r")
        
        # Delay code execution for exactly 1 second
        time.sleep(1)
        seconds -= 1

    print("00:00")
    print("\n⏰ Time's up!")

if __name__ == "__main__":
    start_countdown()
