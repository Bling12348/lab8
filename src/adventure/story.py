from adventure.utils import read_events_from_file
import random

default_message = "You stand still, unsure what to do. The forest swallows you."

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
<<<<<<< HEAD
        return str(Text("You stand still, unsure what to do. The forest swallows you.", style="bold-red"))

def left_path(event):
    text= Text("You walk left. ", style="bold-green") + Text(event, style="italic-yellow")
    return str(text)
def right_path(event):
    text= Text("You walk right. ", style="bold-green") + Text(event, style="italic-yellow")
    return str(text)
=======
        return default_message

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event
>>>>>>> origin/main

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("You wake up in a dark forest. You can go left or right.")
    while True:
<<<<<<< HEAD
        choice = input(
        "Which direction do you choose? *(left/right/exit): ").strip().lower()
        
        if choice == "exit":
            console.print("[bold magenta]You decide to leave the forest. The adventure ends...[/bold magenta]")  
=======
        choice = input("Which direction do you choose? (left/right/exit): ")
        choice = choice.strip().lower()
        if choice == 'exit':
>>>>>>> origin/main
            break
        
        print(step(choice, events))
