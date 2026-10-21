# 🐍 Python Module 02 — Exception Handling

## 📌 Overview

This module focuses on handling errors and exceptions in Python. It explores how to write reliable programs, handle unexpected situations, validate inputs, and prevent errors from terminating program execution unexpectedly.

## 🎯 Learning Objectives

- Understand Python exceptions and runtime errors.
- Use `try` and `except` to handle errors.
- Work with built-in exceptions.
- Raise exceptions using `raise`.
- Create custom exception classes.
- Use `else` and `finally` in exception handling.
- Write more robust and maintainable Python code.

## 🛠️ Technologies

- **Language:** Python 3
- **Version Control:** Git
- **Platform:** 42 Yerevan

## 📂 Project Structure

```text
Python_Module_02/
├── ex00/
│   └── ...
├── ex01/
│   └── ...
├── ex02/
│   └── ...
└── README.md
```

_The structure is illustrative. Adjust it to match the official subject and your repository._

## 📚 Exercises

| Exercise | Description                                            | Status |
| -------- | ------------------------------------------------------ | ------ |
| ex00     | First exercise — update with the official description  | ⬜     |
| ex01     | Second exercise — update with the official description | ⬜     |
| ex02     | Third exercise — update with the official description  | ⬜     |

Update this table with the actual exercise names, requirements, and progress.

## 💡 Key Concepts

### 1. Handling Exceptions

```python
try:
    number = int("42")
except ValueError:
    print("Invalid number")
```

### 2. Raising Exceptions

```python
def check_age(age: int) -> None:
    if age < 0:
        raise ValueError("Age cannot be negative")
```

### 3. Using `finally`

```python
try:
    print("Executing operation")
finally:
    print("Cleanup completed")
```

## ▶️ How to Run

Check your Python version:

```bash
python3 --version
```

Navigate to an exercise directory and run its Python file:

```bash
python3 filename.py
```

Replace `filename.py` with the actual filename required by the exercise.

## 🧠 What I Learned

- [ ] Handle exceptions with `try` and `except`.
- [ ] Understand common built-in exceptions.
- [ ] Raise exceptions to validate data.
- [ ] Create custom exceptions when needed.
- [ ] Use `else` and `finally` appropriately.
- [ ] Debug errors and improve program reliability.

## ✅ Progress

**Status:** In progress 🚧

This module is part of my Python programming journey at 42 Yerevan. Through practical exercises, I am developing my debugging skills and learning to write safer, more reliable Python programs.

## 👤 Author

etamazya

---

_Learning by coding, testing, debugging, and improving every day._
