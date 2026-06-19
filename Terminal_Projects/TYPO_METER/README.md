# Typo_meter

A command-line typing speed test application developed using Python. The program presents a randomly selected paragraph to the user, measures typing speed, calculates typing accuracy, and analyzes typing performance in real time.

## Overview

The application helps users evaluate their typing skills by measuring:

* Typing Speed
* Time Taken
* Total Characters Typed
* Typing Errors

A random paragraph is displayed for each test, making every attempt unique.

## Features

* Random paragraph generation
* Real-time typing timer
* Typing speed calculation
* Error detection system
* Character count analysis
* Performance statistics
* Multiple typing sessions

## Technologies Used

* Python 3
* Time Module
* Random Module
* Functions
* Loops
* String Comparison

## Project Structure

```text id="kl0l57"
Typing-Speed-Tester/
├── main.py
└── README.md
```

## How to Run

```bash id="5v3t9q"
python main.py
```

## Performance Metrics

The application measures:

* Total Time Taken
* Typing Speed (Characters per Second)
* Total Characters Typed
* Number of Typing Errors

## Workflow

1. Start the typing test.
2. Read the displayed paragraph.
3. Type the paragraph as accurately as possible.
4. Submit the text.
5. View performance statistics.

## Concepts Demonstrated

* Time Measurement
* Performance Analysis
* Random Data Selection
* String Comparison
* Error Detection Algorithms
* User Input Processing

## Development Approach

This project was developed from scratch to understand how typing speed testing applications work internally. Speed calculation, error detection, and timing mechanisms were implemented using Python functions and standard libraries.

## Future Improvements

* Words Per Minute (WPM) Calculation
* Accuracy Percentage
* High Score Tracking
* Multiple Difficulty Levels
* Result History
* Graphical User Interface (GUI)
* Leaderboard System
* Custom Paragraph Support

## Note

The current version calculates typing speed based on characters typed per second and compares the entered text with the original paragraph to identify typing mistakes.
