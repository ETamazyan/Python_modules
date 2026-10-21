# 🐍 Python Module 03 — Collections & Data Processing

## 📌 Overview

This module focuses on working with Python data structures and processing data efficiently. Through practical exercises, it develops skills in organizing collections, manipulating data, and building programs that process information from command-line arguments.

## 🎯 Learning Objectives

- Work with lists, tuples, sets, and dictionaries.
- Access, modify, and iterate over collections.
- Understand indexing, slicing, and common collection methods.
- Process command-line arguments using `sys.argv`.
- Use loops and comprehensions to transform data.
- Understand generators and lazy evaluation.
- Write readable, efficient, and maintainable Python code.

## 🛠️ Technologies

- **Language:** Python 3
- **Version Control:** Git
- **Platform:** 42 Yerevan

## 📂 Project Structure

```text
Python_Module_03/
├── ex00/
│   └── ...
├── ex01/
│   └── ...
├── ex02/
│   └── ...
├── ex03/
│   └── ...
└── README.md
```

_This is an example structure. Use the actual folder and file names required by your subject._

## 📚 Exercises

| Exercise | Description                                             | Status |
| -------- | ------------------------------------------------------- | ------ |
| ex00     | First exercise — update with the official description   | ⬜     |
| ex01     | Second exercise — update with the official description  | ⬜     |
| ex02     | Third exercise — update with the official description   | ⬜     |
| ex03     | Fourth exercise — update with the official description  | ⬜     |
| ex04     | Fifth exercise — update with the official description   | ⬜     |
| ex05     | Sixth exercise — update with the official description   | ⬜     |
| ex06     | Seventh exercise — update with the official description | ⬜     |

Update this table to match the exercises in your official subject and track your progress.

## 💡 Key Concepts

### 1. Lists

Lists store ordered collections of elements.

```python
numbers = [10, 20, 30, 40]

numbers.append(50)
print(numbers)
print(numbers[0])
```

### 2. Dictionaries

Dictionaries store data as key-value pairs.

```python
student = {
    "name": "Alex",
    "level": 3
}

print(student["name"])
print(student["level"])
```

### 3. Sets

Sets store unique elements.

```python
numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers)

print(unique_numbers)
```

### 4. List Comprehensions

Comprehensions provide a concise way to create collections.

```python
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]

print(squares)
```

### 5. Command-Line Arguments

The `sys` module provides access to command-line arguments.

```python
import sys

print(sys.argv)
```

### 6. Generators

Generators produce values on demand using `yield`.

```python
def count_up_to(limit):
    for number in range(1, limit + 1):
        yield number

for number in count_up_to(5):
    print(number)
```

_These snippets are illustrative examples, not solutions to the official exercises._

## ▶️ How to Run

Check your Python version:

```bash
python3 --version
```

Navigate to an exercise directory:

```bash
cd Python_Module_03
```

Run the required Python file:

```bash
python3 filename.py
```

Replace `filename.py` with the actual exercise filename. Follow the subject's requirements for command-line arguments and execution.

## 🧠 What I Learned

- [ ] Organize and manipulate data using Python collections.
- [ ] Choose the appropriate data structure for a task.
- [ ] Iterate over and transform collections.
- [ ] Work with command-line arguments.
- [ ] Understand generators and lazy evaluation.
- [ ] Write clear, reusable, and efficient code.
- [ ] Test programs and handle unexpected input.

## ✅ Progress

**Status:** In progress 🚧

This module is part of my Python programming journey at 42 Yerevan. Each exercise helps me improve my understanding of data structures, data processing, and Python programming techniques.

## 👤 Author

42 Yerevan student: etamazya

---

_Learning by coding, testing, and improving one exercise at a time._
