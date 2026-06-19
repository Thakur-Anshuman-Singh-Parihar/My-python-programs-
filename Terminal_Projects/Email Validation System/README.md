# Email Validation System

A Python-based command-line application that validates email addresses using custom validation rules. The program checks the structure of an email address and identifies common formatting errors before determining whether the email is valid.

## Features

* Minimum email length validation
* First character validation
* Single @ symbol verification
* Consecutive dot detection
* Space detection
* Domain format validation
* Invalid character detection
* User-friendly error messages

## Technologies Used

* Python 3
* String Manipulation
* Conditional Statements
* Sets
* Functions

## Project Structure

Email-Validation-System/
├── main.py
└── README.md

## How to Run

Run the application using:

python main.py


## Validation Rules

The application checks:

1. Email length must be greater than 6 characters.
2. The first character must be an alphabet.
3. Only one @ symbol is allowed.
4. Consecutive dots (..) are not allowed.
5. Spaces are not allowed.
6. The domain must contain a valid extension.
7. Invalid characters are not allowed.

## Example

### Valid Email
john123@gmail.com

Output:
valid email

### Invalid Email
123john@gmail.com

Output:
Invalid Email : 1st letter should be an alphabet

## Concepts Demonstrated

* Input Validation
* String Processing
* Pattern Checking
* Function Design
* Conditional Logic

## Future Improvements

* Regular Expression (Regex) Validation
* Support for International Domains
* Email Domain Verification
* Batch Email Validation
* GUI Version using Tkinter

