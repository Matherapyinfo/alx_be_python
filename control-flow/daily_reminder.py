def main():
    task = input("Enter your task: ")
    
    valid_priorities = ['high', 'medium', 'low']
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in valid_priorities:
            break
        print("Invalid priority. Please enter high, medium, or low.")
    
    valid_time_bound = ['yes', 'no']
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in valid_time_bound:
            break
        print("Invalid input. Please enter yes or no.")
    
    match priority:
        case 'high' | 'medium':
            base_message = f"Reminder: '{task}' is a {priority} priority task"
        case 'low':
            base_message = f"Note: '{task}' is a low priority task"
    
    if time_bound == 'yes':
        final_message = base_message + " that requires immediate attention today!"
    else:
        if priority == 'low':
            final_message = base_message + ". Consider completing it when you have free time."
        else:
            final_message = base_message + "."
    
    print("\n" + final_message)

if __name__ == "__main__":
    main()
