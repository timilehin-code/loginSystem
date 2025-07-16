from rich.prompt import Prompt
from rich.console import Console
from auth import menu, register,login

prompt = Prompt()
console = Console()

menu()


option = prompt.ask("[blue]Choose an option between 1 & 2[/blue]").strip()

if option == "1":
    register()
elif option == "2":
   login()
else:
    console.print("[red]invalid Input![/red]")