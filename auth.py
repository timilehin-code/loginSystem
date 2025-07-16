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
    if len(password) < 8:
        console.print("[red]Password must be at least 8 characters long.[/red]")
        return False
    if not re.search(r"[A-Z]", password):
        console.print("[red]Password must contain at least one uppercase letter.[/red]")
        return False
    if not re.search(r"[a-z]", password):
        console.print("[red]Password must contain at least one lowercase letter.[/red]")
        return False
    if not re.search(r"\d", password):
        console.print("[red]Password must contain at least one digit.[/red]")
        return False
    if not re.search(r"[!@#$%^&*()_+]", password):
        console.print("[red]Password must contain at least one special character.[/red]")
        return False
    return True


# password hasher
def hash_password(password):
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hash_password.decode("utf-8")

# compare passwords 
def compareHash(input, hashedPassword):
    try:
        return bcrypt.checkpw(input.encode("utf-8"), hashedPassword)
    except Exception as e:
        console.print(f"[red]Error verifying password: {e}[/red]")
        return False

# check if email exist
def checkEmail(usersList, email):
    for user in usersList:
        for value in user.values():
            if email in str(value):
                return True
    return False


def generate_random_string(length):
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def matchpassword(a, b):
    if a == b:
        return True
    else:
        return False


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
    email = prompt.ask("[yellow]Input your email[/yellow]").strip().lower()
    passWord = getpass.getpass("[yellow]Input your Password[/yellow]").strip()
    confirmPassword = getpass.getpass("[yellow]Enter password again[/yellow]")
    randInt = random.randint(00, 99)
    details = {
        "First_Name": fName,
        "Last_Name": lNname,
        "email": email,
        "userName": fName + "_" + generate_random_string(3) + str(randInt),
        "password": hash_password(passWord),
    }

    if not validate_email(email):
        console.print("[red]your email  is invalid![/red]")
        return
    elif not validate_password(passWord):
        console.print(
            "[red]your password is invalid! Must be 8+ characters with uppercase,lowercasem digit, and a special character.[/red]"
        )
        return
    elif checkEmail(loaded_users, email):
        console.print("[red]The email you entered already exist![/red]")
        return
    elif checkEmail(loaded_users, details["userName"]):
        console.print("[red]The UserName already exist![/red]")
        return
    elif not matchpassword(passWord, confirmPassword):
        console.print("[red]Pasword does not match.[/red]")
        return
    else:
        loaded_users.append(details)
        console.print("[green]You have be registered siccessfully![green]")
        console.print(f"[blue]Your username is {details['userName']}[/blue]")

    try:
        with open("users.json", "w") as usersFile:
            json.dump(loaded_users, usersFile, indent=4)
    except Exception as e:
        print(f"Error saving users to file: {e}")


# user login
def login():
    load_users = []
    try:
       with open("users.json", "r") as Users:
            load_users = json.load(Users)
    except (FileNotFoundError, json.JSONDecodeError):
            console.print("[red]No User registerd yet.[/red]")
            return

    UserName = prompt.ask("[cyan]enter your user name:[/cyan]")
    password = getpass.getpass("[cyan]Enter your password [/cyan]")
    if not validate_password(password):
        return
    for user in load_users:
        if user['userName'].lower() == UserName.lower() and compareHash(password, user['password'].encode('utf-8')) :
            console.print(f"[blue]Welcome {user["First_Name"]}[/blue]")
        else:
           console.print("[red]Incorrect login details[/red]")