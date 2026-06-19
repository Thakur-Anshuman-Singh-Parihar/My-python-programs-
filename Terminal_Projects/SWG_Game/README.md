# Snake Water Gun Game

A command-line implementation of the classic Snake Water Gun game developed using Python. The game allows a player to compete against the computer across multiple rounds while maintaining scores and determining an overall winner.

## Overview

Snake Water Gun is a variation of Rock Paper Scissors where:

* Snake drinks Water
* Water disables Gun
* Gun defeats Snake

The winner is determined based on the outcome of each round.

## Features

* Computer-generated random moves
* 10-round gameplay system
* Real-time score tracking
* Winner announcement after each round
* Final match result calculation
* Multiple input formats supported
* User-friendly interface with game rules

## Technologies Used

* Python 3
* Random Module
* Loops
* Conditional Statements
* Input Handling

## Project Structure

Snake-Water-Gun-Game/
├── main.py
└── README.md

## How to Run

python main.py

## Game Rules

| Player Choice | Computer Choice | Winner |
| ------------- | --------------- | ------ |
| Snake         | Water           | Snake  |
| Snake         | Gun             | Gun    |
| Water         | Gun             | Water  |

The match consists of 10 rounds, and the player with the highest score at the end wins the game.

## Supported Inputs

The game accepts multiple input formats:

```text
Snake : snake, s, 1
Water : water, w, 2
Gun   : gun, g, 3
```

## Concepts Demonstrated

* Randomized Game Logic
* Score Management
* Menu Driven Interaction
* User Input Validation
* Conditional Decision Making
* Loop Control

## Development Approach

This project was developed from scratch to practice game logic implementation, random event generation, score tracking, and user interaction in Python without relying on external libraries.

## Future Improvements

* Best of 3 / Best of 5 Modes
* Difficulty Levels
* Player Statistics
* Multiplayer Mode
* GUI Version using Tkinter
* Leaderboard System
* Save Match History
