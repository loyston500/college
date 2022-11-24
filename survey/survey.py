# Code for survey regarding bad habits by group 17, I BCA A
from pprint import pprint 
from statistics import mean, mode

print("Welcome! This is a survey regarding bad habits among youth. By group 17, I BCA A")

responses = []
bad_habits = [
    "Being lazy",
    "Oversleeping/Not getting enough sleep",
    "Unhealthy eating or poor diet", 
    "Excessive social media usage",
    "Procrastination (not doing work in time)", 
    "Not being open or hiding your feelings",
    "Being irresponsible",
    "Poor hygiene",
    "Being an addict",
]

while input("Type y to start/continue the survey: ").lower() == "y":
    response = {}
    
    response["name"] = input("Enter your name (optional): ").strip()
    response["regno"] = input("Enter your reg no (optional): ").strip()
    response["course"] = input("Enter your course Ex: BA, BCA, B.SC etc..: ").strip().upper()
    response["bad_habits"] = []

    ans = input("Do you have any bad habits? Answer yes or no: ").lower()
    if ans == "yes":
        print("What are they? Mention all that apply, if not leave blank. Ex: 1 2 3")
        for n, habit in enumerate(bad_habits):
            print(f"{n + 1}. {habit}")
        
        try:
            for n in [int(n) - 1 for n in input("Your answer: ").split()]:
                response["bad_habits"].append(bad_habits[n])

            other = input("If you have any other bad habits please enter, if not leave blank: ").strip()
            if other: 
                response["bad_habits"].append(other)

            if not response["bad_habits"]:
                print("Need at least one habit. Please retry from the beginning.")
                continue
        except:
            print("Invalid input, please retry from the beginning.")
            continue

    elif ans == "no":
        pass

    else:
        print("Invalid input, please retry from the beginning.")
        continue

    responses.append(response)
    print("Thank you for filling up the survey! Next person please!")


# calculation
total = len(responses)

with_bad_habits = list(response for response in responses if response["bad_habits"])
print(f"Total particpants: {len(total)}\nParticpants with bad habit: {len(with_bad_habit)}")

with_name_regno = list(response for response in responses if response["name"] or response["regno"])
print(f"Participants who were comfortabile putting their name or regno: {len(with_name_regno)}")

counts = {habit: 0 for habit in bad_habits}
for response in responses:
    for habit in response["bad_habits"]:
        count[habit] += 1

for habit, count in counts.items():
    print(f"{habit}: {count}")