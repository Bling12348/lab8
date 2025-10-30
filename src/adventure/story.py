from adventure.utils import read_events_from_file
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
import random

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    elif choice== "exit":
        return str(Text("You decide to leave the forest. The adventure ends...", style="bold-magenta"))
    else:
        return str(Text("You stand still, unsure what to do. The forest swallows you.", style="bold-red"))

def left_path(event):
    text= Text("You walk left. ", style="bold-green") + Text(event, style="italic-yellow")
    return str(text)
def right_path(event):
    text= Text("You walk right. ", style="bold-green") + Text(event, style="italic-yellow")
    return str(text)

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    console.print("[bold yellow]You wake up in a dark forest.[/bold yellow]")
    console.print("[italic]You can go left or right.[/italic]")    
    while True:
        choice = Prompt.ask("[bold red]Which direction do you choose?[/bold red]", choices=["left","right","exit"], default="exit")
        choice = choice.strip().lower()
        
        if choice == "exit":
            console.print("\n[bold magenta]You decide to leave the forest. The adventure ends...[/bold magenta]")  
        break
        
        story_output = step(choice, events)
        console.print(story_output)
        console.print("")