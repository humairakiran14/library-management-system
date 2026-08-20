# Library Management System

An advanced, object-oriented Library Management System built in Python with SQLite storage, secure login, and full book/member management. Built as part of the Python Development Internship at Aptura Tech Solutions (Batch 02, Week 2) — scored 99/100.

## Features

- **Book & Member Management** — add, update, and track books and members
- **Issue & Return Books** — full book issue/return workflow
- **Fine Calculation** — automatically calculates late fines based on a 14-day due period (Rs.10/day late)
- **Secure Login** — password-protected login using hashed passwords (via `hashlib`), with a limit of 3 login attempts
- **Search & Filter** — look up books and members quickly
- **Custom Exceptions** — dedicated exception classes for clear, specific error handling
- **Logging System** — timestamped INFO/ERROR logs written to `library.log` for tracking activity and debugging

## Tech Stack

- Python 3 (Object-Oriented Programming)
- SQLite (`library.db`) for persistent storage
- `hashlib` for password hashing
- Python's built-in `logging` module

## Architecture

The system is built around three core classes:

- **`Book`** — represents a book and its attributes (title, author, availability, etc.)
- **`Member`** — represents a library member and their borrowing activity
- **`Library`** — manages the overall system, holding a live SQLite connection and coordinating the `books`, `members`, and `issued_books` tables

This was the first project where OOP concepts — classes, objects, `self`, `__init__` — were applied, learned hands-on while building it.

## How It Works

- `Library` maintains a persistent connection to `library.db`, with three tables: `books`, `members`, and `issued_books`
- Login requires a correct hashed password, with up to 3 attempts before lockout
- When a book is returned late, the system calculates a fine automatically based on days overdue × Rs.10, using the 14-day due period as the baseline
- All significant actions and errors are logged with timestamps to `library.log` via custom exception handling and the logging module

## Getting Started

```bash
python library_management.py
```

On first run, the SQLite database (`library.db`) and log file (`library.log`) will be created automatically.

## Project Notes

This project was a step up from a purely functional, file-based system (see the [Student Record Management System](../student-management-system-python)) toward a structured, class-based design with a real database backend, authentication, and proper error handling and logging — the kind of foundation production-style applications are built on.

## Author

Humaira Kiran
