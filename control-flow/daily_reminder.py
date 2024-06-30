task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
prio_reminder = f"'{task}' is a {priority} priority task that requires immediate attention today!"
non_reminder = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."

match priority:
    case "high" : 
        if time_bound == "yes":
            print("Reminder:",prio_reminder)
        else:
            print("Note:",non_reminder_reminder)
    case "medium": 
        if time_bound == "yes":
            print("Reminder:",prio_reminder)
        else:
            print("Note:",non_reminder)
    case "low": 
        if time_bound == "yes":
            print("Reminder:",prio_reminder)
        else:
            print("Note:",non_reminder)