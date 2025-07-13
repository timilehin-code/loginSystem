from rich.prompt import Prompt
from rich.console import Console
import json
import os
import re
import bcrypt

prompt = Prompt()
console = Console()

def menu():
    console.print(
        "[bold blue]welcome to the authentication, please select the an option[/bold blue]"
    )
    console.print("[green]1.Register[/green]")
    console.print("[green]2.Login[/green]")
# email vaidator
def validate_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

# password validator
def validate_password(password):
    password_regex = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?\d)(?=.*?[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+-]{8,}$"
    return bool(re.match(password_regex, password))

# password hasher
def hash_password(password):
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hash_password.decode('utf-8')
# user registration
def register():
    loaded_users = []
    if os.path.exists("users.json"):
        try:
            with open("users.json", "r") as usersFile:
                loaded_users = json.load(usersFile)
                console.print(f"users loaded successfully")
        except Exception as e:
            loaded_users = []
            console.print(f"[red]unable to print users because, {e},[/red]")
    fName = prompt.ask("[yellow]Input your first name[/yellow]")
    lNname = prompt.ask("[yellow]Input your Last name[/yellow]")
    email = prompt.ask("[yellow]Input your email[/yellow]")
    passWord = prompt.ask("[yellow]Input your Password[/yellow]")

    details = {
        "First_Name": fName,
        "Last_Name": lNname,
        "email": email,
        "password": hash_password(passWord),
    }

    if validate_email(email) and validate_password(passWord):
        loaded_users.append(details)
    else:
        raise ValueError("[red]your email or password is invalid![/red]")            

    try:
        with open("users.json", "w") as usersFile:
            json.dump(loaded_users, usersFile, indent=4)
    except Exception as e:
        print(f"Error saving users to file: {e}")



