import datetime

# Initialize the logger
print("--- Task Logger Started ---")
print("Type 'exit' to stop logging.")

while True:
    # Get the user's action
    action = input("\nEnter an action you performed: ")
    
    # Check if the user wants to quit
    if action.lower() == 'exit':
        print("Exiting logger. Check 'task_log.txt' for your history.")
        break
    
    # Generate timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Action: {action}\n"
    
    # Append the entry to a text file
    with open("task_log.txt", "a") as file:
        file.write(log_entry)
        
    print("Action logged successfully!")