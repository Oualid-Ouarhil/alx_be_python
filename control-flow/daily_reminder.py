task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_intens = input("Is it time-bound? (yes/no):")
error_mess = "something went wrong!"
first_part = f"{task} is a {priority} priority task"

match priority:
    case "high":
        reminder = "that requires immediate attention today!"
    case "medium":
       reminder = "schedule it for later"
    case "low":
        reminder = "Consider completing it when you have free time."
    case _ :
        message = error_mess

if time_intens == "yes":
    reminder = "that requires immediate attention today!"
elif time_intens == "no":
    reminder = "Consider completing it when you have free time."
else:
    message = error_mess

message = (f"Reminder: '{task}' is a {priority} priority task. that requires immediate attention today!" 
           if time_intens == "yes" else "Consider completing it when you have free time.")
print("Reminder: ", reminder)
print(message)
