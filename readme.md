# User Authentication system with python

## overview
This is a simple light weight login system that works on the terminal it allow users to be  onboarded and also autenticate users when trying to login 


## Features
- User onbording
- User autentication
- password encryption using `utf-8` hashing
- saving of registered users
- password validation
- checking email validation
- secure login
- email authentication

## Requirements
- **Python**: Version 3.7 or later
- Intermidate Understanding of python
- Proper Understanding of how python functions works

## Dependencies
- `Json` for saving users info
- `bcrypt` for data encryption
- `re` for regular expresion validation
- `rich` for terminal styling
- `os` for file handling
- `string` for random characters
- `random` to genrate random numbers and letters
- `smtplib` to send mail
- `email` for mail handling 
- `dotenv` for accesing the environment variable (`.env`) file



## Usage
Ensure python is installed on your computer and run the `main.py` file.

## installation
1. Ensure Python 3.7 or higher is installed on your machine. Verify with:

   ```bash
    python --version
   ```
2. Clone the repository :

   ```bash
   git clone https://github.com/timilehin-code/loginSystem.git
   ```
3. Navigate to the project directory:
   ```bash
   cd loginSystem
   ```
4. make sure the python rich module is installed on your machine. to install run the following command on your terminal:

```bash
  pip install rich
```

4.  make sure the python bcrypt module is installed on your machine. to install, run the following command on your terminal:

```bash
  pip install bcrypt
```

5. make sure the python `dotenv` module is installed on your machine. to install, run the following command on your terminal:

```bash
  pip install python-dotenv
```

6. also make sure you create a `.env` file to store your email credentials

```env
EMAIL_ADDRESS=yourmail@mail.com
EMAIL_PASSWORD=yourPassword
```


## project Structure

```
loginSystem/
|
|__.gitignore #gitignore file
|
|__auth.py  #all functions file
|
|__main.py #menu file
|
└──  README.md #this file
```
# Note
Don't use this directly on your project as it is still a working progress, and more updates will be added soon thanks. Oluwatimilehin ☺️❤️💙