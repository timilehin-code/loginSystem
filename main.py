from rich.prompt import Prompt
from auth import menu, register

prompt = Prompt()

menu()


option = prompt.ask("[blue]Choose an option between 1 & 2[/blue]").strip()

if option == "1":
    register()
if option == "2":
    print("login is still a work in progress")
