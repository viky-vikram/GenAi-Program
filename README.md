# Grade Calculator

A simple Python application that converts a student's mark into a grade based on a predefined grading scale.

## Features

* Accepts marks from the user
* Validates input range (0–100)
* Calculates grades automatically
* Handles invalid inputs gracefully
* Uses only Python standard library

## Grading Scale

| Mark Range | Grade |
| ---------- | ----- |
| 90 - 100   | A     |
| 80 - 89    | B     |
| 70 - 79    | C     |
| 60 - 69    | D     |
| Below 60   | E     |

## Requirements

* Python 3.x

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/viky-vikram/GenAi-Program.git
```

2. Navigate to the project directory:

```bash
cd GenAi-Program
```

3. Run the program:

```bash
python grade_system.py
```

## Sample Output

### Valid Input

```text
=== Grade Calculator ===
Enter mark (0-100): 85

Result
------
Mark Entered : 85.0
Grade        : B
```

### Invalid Range

```text
=== Grade Calculator ===
Enter mark (0-100): 120

Error: Mark must be between 0 and 100.
```

### Invalid Input

```text
=== Grade Calculator ===
Enter mark (0-100): abc

Error: Please enter a valid numeric value.
```

## Project Structure

```text
GenAi-Program/
│
├── grade_system.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Concepts Used

* Variables
* Functions
* Conditional Statements (if-elif-else)
* User Input
* Exception Handling (try-except)
* Data Validation

## Author

Vikram M
