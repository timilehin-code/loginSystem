# User Authentication System with Python

## Overview
This is a lightweight, terminal-based user authentication system that allows users to register (onboarding) and log in securely.

## Features
- **User Onboarding**: Register new users with a valid email and secure password.
- **User Authentication**: Log in with email and password, with secure validation.
- **Password Hashing**: Securely hash passwords using `bcrypt` for safe storage.
- **User Data Storage**: Save registered user information in a JSON file.
- **Password Validation**: Enforce strong password requirements (e.g., minimum length, special characters).
- **Email Validation**: Verify email format using regular expressions.
- **Secure Login**: Authenticate users securely with hashed password verification.
- **Email Authentication**: Send verification emails during registration or for password recovery (requires email setup in `.env`).

## Requirements
- **Python**: Version 3.7 or later
- Intermediate understanding of Python
- Basic understanding of Python functions

## Dependencies
- Python standard libraries: `json`, `re`, `os`, `string`, `random`, `smtplib`, `email`
- External packages:
  - `rich` for terminal styling
  - `bcrypt` for password hashing
  - `python-dotenv` for accessing environment variables (`.env` file)


## Installation
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
4. Install the required external packages:

```bash
 pip install rich bcrypt python-dotenv
```


5. Create a .env file in the project root with the following structure:

```env
EMAIL_ADDRESS=yourmail@mail.com
EMAIL_PASSWORD=yourPassword
```
**Note**:  Ensure the `.env` file is added to `.gitignore` to prevent committing sensitive credentials. For Gmail, enable 2FA and use an app-specific password for `EMAIL_PASSWORD`

6. The following dependencies are part of Python’s standard library and do not require installation:  `json`, `re`, `os`, `string`, `random`, `smtplib`, `email`


## Usage
Ensure python is installed on your computer .

1. Navigate to the project directory:
   ```bash
   cd loginSystem
   ```
2. Run the main Script
   ```bash
   python main.py
   ```
3. Follow the terminal prompts to register a new user, log in, or exit the program.

## project Structure

```
loginSystem/
|
|__.gitignore         # Gitignore file
|
|__.env              # Environment file for email credentials (not included, must be created)
|
|__auth.py           # All authentication functions
|
|__main.py           # Terminal menu interface
|
└── README.md        # This file
```
# Note
This project is a work in progress. Features like password recovery, advanced email verification, and user profile management may be added in future updates. Do not use this in production without thorough testing. Contributions and feedback are welcome! Thanks, Oluwatimilehin ☺️❤️💙