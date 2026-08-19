# Secure Coding Review
## Library Management System

### 1. Project Overview

This project is a Library Management System developed using Python and Tkinter.

The application provides:
- User and Admin login
- Dashboard
- Book management
- Book search
- Borrow book
- Return book
- Add book
- Remove book

### 2. Programming Language

Python

### 3. GUI Framework

Tkinter

---

# Security Findings

## Finding 1: Hardcoded Credentials

### Vulnerability

The application stores usernames and passwords directly in the source code.

Example:

```python
if username == "admin" and password == "admin123":
