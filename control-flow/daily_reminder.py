task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").lower()

time_inten = input("Is it time-bound? (yes/no): ").lower()

first_reminder = f"'{task}' is a {priority} priority task that requires immediate attention today!"

second_reminder = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."

match priority:
    case "high" : 
        if time_inten == "yes":
            print("Reminder:",first_reminder)
        else:
            print("Note:",second_reminder)
    case "medium": 
        if time_inten == "yes":
            print("Reminder:",first_reminder)
        else:
            print("Note:",second_reminder)
    case "low": 
        if time_inten == "yes":
            print("Reminder:",first_reminder)
        else:
            print("Note:",second_reminder)
