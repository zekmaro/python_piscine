# 🐍 Python Piscine — 42 School

Welcome to my 42 Python Piscine repository. This repository contains my solutions and exercises from the Python Piscine at 42, organized by project. Each project is designed to build both foundational and advanced skills in Python programming, progressing from basics to object-oriented design and data manipulation.

---

## 📁 Project Overview

### `00 - Starting`
**Goal**: Get comfortable with the Python environment, basic syntax, types, and simple logic.

- Handling command-line arguments
- String formatting
- Type checking and assertions
- Simple input/output
- Functional programming basics (e.g., `filter`, `map`, `lambda`)

---

### `01 - Array`
**Goal**: Learn to manipulate images and matrices using NumPy and Pillow.

- Load and inspect image data as NumPy arrays
- Slice and reshape 2D and 3D arrays
- Convert RGB channels and display images
- Perform basic image transformations (e.g., transpose, zoom, extract red channel)
- Visualize with `matplotlib`

---

### `02 - DataTable`
**Goal**: Work with tabular data using Pandas and NumPy.

- Load `.csv` datasets
- Analyze and clean missing data
- Filter rows/columns
- Apply custom operations per column
- Summarize with groupby, describe, mean, etc.
- Format and present tabular results

---

### `03 - OOP`
**Goal**: Practice object-oriented programming and data encapsulation.

- Define and use classes and methods
- Implement special methods (`__str__`, `__repr__`, etc.)
- Understand inheritance and polymorphism
- Create reusable, testable structures (e.g., custom matrix or data models)
- Possibly simulate real-world behavior using class logic

---

### `04 - Dod` (Data-Oriented Design)
**Goal**: Optimize data and processing by separating logic from structure.

- Work with raw data and transform it through pipelines
- Avoid class-based hierarchies in favor of flat data + pure functions
- Emphasize performance, minimal coupling, and clear transformation logic
- Simulate DOD techniques often used in games, graphics, or batch processing

---

## 📦 Technologies Used

- Python 3.11+
- NumPy
- Pillow
- Pandas
- Matplotlib
- (No external tools beyond standard data/image libs unless allowed)

---

## 📚 How to Run

Each folder contains its own `tester.py` or examples. For example:

```bash
cd ex01
python3 tester.py
