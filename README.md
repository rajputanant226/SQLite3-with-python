📘 Python + SQLite3 Database Guide

A complete beginner-friendly guide to using SQLite3 with Python for creating real database-driven applications.

📌 Introduction

SQLite3 is a lightweight, serverless, file-based relational database engine.
Python provides a built-in module sqlite3 which makes it extremely easy to:

Create databases

Run SQL queries

Perform CRUD operations

Build real-world apps without installing any external database

This README covers everything you need to quickly get started.

🔥 Why SQLite3?

No installation required

Single .db file stores everything

Beginner-friendly

Fast and lightweight

Perfect for college projects

Easy to migrate to MySQL later

Works seamlessly with Python

🏗️ Getting Started
✔️ 1. Import the SQLite3 module
import sqlite3

✔️ 2. Create / Connect to a Database
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()


If file mydatabase.db doesn’t exist, Python will automatically create it.

✔️ 3. Create a Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")
conn.commit()

🔄 CRUD Operations
✔️ 4. Insert Data
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
               ("Anant", 21, "B.Tech IT"))
conn.commit()

✔️ 5. Fetch Data
Fetch all rows:
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

Fetch one row:
cursor.execute("SELECT * FROM students WHERE id = 1")
print(cursor.fetchone())

✔️ 6. Update Data
cursor.execute("UPDATE students SET age = 22 WHERE id = 1")
conn.commit()

✔️ 7. Delete Data
cursor.execute("DELETE FROM students WHERE id = 1")
conn.commit()

✔️ 8. Close the Connection
conn.close()

🔍 Real-World Project Ideas (Python + SQLite3)
You can build fully working apps like:

Notes App

Todo List App

Expense Tracker

Library Management System

Student Records System

Password Manager

Inventory Management App

All these projects require CRUD operations — and SQLite3 fits perfectly!

🎯 Best Practices

Always use ? placeholder to prevent SQL Injection

Use CREATE TABLE IF NOT EXISTS for safe table creation

Always commit after INSERT/UPDATE/DELETE

Close the database connection at the end

Use functions for cleaner code structure

For larger projects, structure code using MVC or modular files

🚀 Summary

With SQLite3 + Python you can:

✔ Create databases easily
✔ Perform CRUD operations
✔ Build real applications
✔ Understand SQL fundamentals
✔ Prepare for advanced databases like MySQL & PostgreSQL

SQLite3 is the best starting point for mastering database concepts as a beginner.
