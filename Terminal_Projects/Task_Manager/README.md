# Task Manager

A command-line task management application developed using Python. The system allows users to create, track, update, and organize daily tasks through a menu-driven interface.

## Overview

The application helps users manage their work efficiently by maintaining separate lists for:

* All Tasks
* Pending Tasks
* Completed Tasks

Users can update task status, remove tasks, and monitor their progress directly from the terminal.

## Features

### Task Management

* Add new tasks
* View all tasks
* View completed tasks
* View pending tasks

### Task Status Tracking

* Mark pending tasks as completed
* Automatically move tasks between categories
* Separate task lists for better organization

### Task Deletion

* Delete pending tasks
* Delete completed tasks
* Delete tasks from the master task list

## Technologies Used

* Python 3
* Lists
* Loops
* Conditional Statements
* Menu Driven Programming

## Project Structure

Task-Manager/
├── main.py
└── README.md

## How to Run

python main.py

## Available Operations

| Option | Function             |
| ------ | -------------------- |
| 1      | Add Task             |
| 2      | View All Tasks       |
| 3      | View Completed Tasks |
| 4      | View Pending Tasks   |
| 5      | Update Task Status   |
| 6      | Delete Task          |
| 7      | Exit                 |

## Concepts Demonstrated

* CRUD Operations
* List Management
* Status Tracking Systems
* Menu Driven Applications
* User Input Handling
* Data Organization

## Development Approach

This project was developed from scratch using Python lists and custom task management logic. The goal was to understand how real-world productivity applications manage task creation, status updates, and task categorization without relying on external libraries or databases.

## Future Improvements

* File Handling for Persistent Storage
* Due Date Support
* Task Priority Levels
* Search Functionality
* Task Categories
* Data Export
* GUI Version using Tkinter
* SQLite Database Integration

## Note

Currently, task data is stored in memory and resets when the program is closed. Future versions can use file handling or databases to provide permanent storage.
