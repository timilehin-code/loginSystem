from rich.prompt import Prompt
from rich.console import Console
import json
import os
import re
import bcrypt
import random
import string
import getpass

prompt = Prompt()
console = Console()

# list of options
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
    hash_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hash_password.decode("utf-8")


# check if email exist
def checkEmail(usersList, email):
    for user in usersList:
        for value in user.values():
            if email in str(value):
                return True
    return False

def genrate_random_string(length):
    return "".join(random.choice(string.ascii_letters)for _ in range(length)) 
    
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
    fName = prompt.ask("[yellow]Input your first name[/yellow]").strip().title()
    lNname = prompt.ask("[yellow]Input your Last name[/yellow]").strip().title()
    email = prompt.ask("[yellow]Input your email[/yellow]").strip()
    passWord = prompt.ask("[yellow]Input your Password[/yellow]").strip()
    randInt = random.randint(00,99)
    details = {
        "First_Name": fName,
        "Last_Name": lNname,
        "email": email,
        "userName": fName + "_" + genrate_random_string(3)+ str(randInt),
        "password": hash_password(passWord),
    }

    if not validate_email(email):
        console.print("[red]your email  is invalid![/red]")
        return
    elif not validate_password(passWord):
        console.print("[red]your password is invalid! Must be 8+ characters with uppercase,lowercasem digit, and a special character.[/red]")
        return
    elif checkEmail(loaded_users, email):
        console.print("[red]The email you entered already exist![/red]")
        return
    else:
        loaded_users.append(details)

    try:
        with open("users.json", "w") as usersFile:
            json.dump(loaded_users, usersFile, indent=4)
    except Exception as e:
        print(f"Error saving users to file: {e}")
