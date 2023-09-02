import time
import threading

# Function to update the countdown
def update_countdown():
    global remaining_time
    while remaining_time > 0 and not stop_timer:
        time.sleep(1)
        remaining_time -= 1
        print(format_time(remaining_time))
    if not stop_timer:
        print("Time's up!")
        
        

# Function to start the countdown
def start_countdown():
    global remaining_time, stop_timer
    if not stop_timer:
        return
    input_time = int(input("Enter countdown time in seconds: "))
    remaining_time = input_time
    stop_timer = False
    countdown_thread = threading.Thread(target=update_countdown)
    countdown_thread.start()

# Function to reset the countdown
def reset_countdown():
    global remaining_time, stop_timer
    stop_timer = True
    remaining_time = 0

# Function to format time in MM:SS format
def format_time(seconds):
    minutes = seconds // 60
    seconds %= 60
    return f"{minutes:02d}:{seconds:02d}"

# Initialize variables
remaining_time = 0
stop_timer = True

# Main loop
while True:
    print("\nCountdown Timer")
    print("1. Start Countdown")
    print("2. Reset Countdown")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        start_countdown()
    elif choice == '2':
        reset_countdown()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please select again.")

print("Goodbye!")
