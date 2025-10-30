from adventure.utils import read_events_from_file
from rich.console import Console
from rich.text import Text
import random

default_message = "You stand still, unsure what to do. The forest swallows you."

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return str(left_path(random_event))
    elif choice == "right":
        return str(right_path(random_event))
    else:
        return str(default_message)

def left_path(event):
    text= Text("You walk left. ", style="bold-green") + Text(event, style="italic-yellow")
    return str(text)
def right_path(event):
    text= Text("You walk right. ", style="bold-green") + Text(event, style="italic-yellow")
    return str(text)

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    console.print("[bold yellow]You wake up in a dark forest. You can go left or right.[/bold yellow]")
    while True:
        choice = input(
        "Which direction do you choose? *(left/right/exit): ").strip().lower()
        
        if choice == "exit":
            print("[bold magenta]Goodbye! You decide to leave the forest. The adventure ends...[/bold magenta]")  
            break
        
        print(step(choice, events))
        console.print(story_output)
        console.print("")