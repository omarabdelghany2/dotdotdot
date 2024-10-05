import schedule
import time

def print_hello():
    print("Hello")

# Schedule the task to run every hour
schedule.every(1).hours.do(print_hello)

while True:
    # Run pending tasks
    schedule.run_pending()
    # Sleep for a while to prevent high CPU usage
    time.sleep(1)