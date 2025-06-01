# daily_reminder.py

def get_task():
    task = input("Enter your task: ").strip()
    return task

def get_priority():
    valid_priorities = ["high", "medium", "low"]
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in valid_priorities:
            return priority
        print("Invalid priority. Please enter high, medium, or low.")

def get_time_bound():
    valid_answers = ["yes", "no"]
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in valid_answers:
            return time_bound
        print("Invalid input. Please enter yes or no.")

def main():
    task = get_task()
    priority = get_priority()
    time_bound = get_time_bound()

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Please complete it as soon as possible.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Try to get it done soon.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()
