# Car Showroom Management System

A console-based car showroom management application developed using Python. The system provides separate functionalities for showroom staff and customers, allowing vehicle management, inventory browsing, purchasing, and test drive booking through a menu-driven interface.

## Overview

The application simulates the operations of a car dealership by providing:

* Owner/Staff Management
* Vehicle Inventory Management
* Customer Vehicle Search
* Vehicle Purchase System
* EMI Calculation
* Test Drive Booking

## Features

### Owner / Staff Features

* Password Protected Access
* Add New Cars
* Update Vehicle Prices
* Delete Vehicles
* Change System Password

### Customer Features

* View Available Cars
* Search Cars by:

  * Name
  * Vehicle Type
  * Engine Type
  * Budget
  * Seating Capacity
* Purchase Vehicles
* EMI Calculation
* Test Drive Requests

## Technologies Used

* Python 3
* Lists
* Dictionaries
* Functions
* Conditional Statements
* Loops

## Project Structure

Car-Showroom-Management/
├── main.py
└── README.md


## How to Run

Run the project using:

bash
python main.py


## Sample Vehicle Information

The application contains sample vehicle records including:

* Scorpio
* Verna
* Swift

Each vehicle stores:

* Model Name
* Vehicle Type
* Engine Type
* Mileage
* Manufacturing Year
* Features
* Price
* Seating Capacity
* Available Colors

## Purchase System

Customers can purchase vehicles using:

* EMI
* Cheque
* Cash

The EMI option automatically calculates:

* Down Payment (30%)
* Monthly EMI for 24 Months

## Test Drive Feature

Customers can request a test drive for available vehicles.

The system displays:

* Security Deposit Amount
* Documentation Instructions
* Test Drive Duration

## Concepts Demonstrated

This project demonstrates the practical use of:

* Menu Driven Programming
* Data Management using Dictionaries
* CRUD Operations
* User Authentication
* Search Functionality
* Payment Processing Logic
* Python Functions and Loops

## Future Improvements

* File Handling for Permanent Data Storage
* Database Integration (SQLite/MySQL)
* Customer Records Management
* Sales Report Generation
* GUI Version using Tkinter
* Invoice Generation
* Admin Activity Logs


