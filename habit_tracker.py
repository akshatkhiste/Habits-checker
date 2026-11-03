import json
import os

def load_habits():
    if os.path.exists("habits.json"):
        with open("habits.json", "r") as f:
            return json.load(f)
    return {}
def save_habits(habits):
    with open("habits.json", "w") as f:
        json.dump(habits, f)

habits = load_habits()
while True:
    print("Current habits:", habits)
    cmd = input("1[1] add habit \n [2] view habits \n [3] mark complete \n [4] exit  ")
    if cmd == "1":
        habit = input('Enter the habit: ')
        habits[habit] = False
        save_habits(habits)
        print("Habit added successfully.")
    if cmd == '2':
        if not habits:
            print('no habits available')
        else:
            for habit, done in habits.item():
                print(f'{habit}{done}')



    if cmd == '3':
        name = input('which habit would you like to mark complete?')
        habits[name] = True
        save_habits(habit)
    if cmd == '4':
        break


    