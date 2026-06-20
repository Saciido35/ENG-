#  Student Management System

A simple and beginner-friendly **Student Management System** built using **MySQL (XAMPP / phpMyAdmin)**.  
This project demonstrates basic **CRUD operations** (Create, Read, Update, Delete) using SQL.


# Project Overview

This system allows users to manage student records efficiently.  
It supports adding new students, viewing stored data, updating records, and deleting entries.



# Technologies Used

- XAMPP (Apache Server)
- MySQL / phpMyAdmin
- SQL (Structured Query Language)



#  Database Information

- **Database Name:** `student_db`
- **Table Name:** `students`



# Database Schema

| Column       | Data Type        | Description                          |
|--------------|------------------|--------------------------------------|
| id           | INT              | Primary Key, Auto Increment          |
| name         | VARCHAR(100)     | Student full name                    |
| age          | INT              | Student age                         |
| department   | VARCHAR(100)     | Student department/field of study   |
| created_at   | TIMESTAMP        | Record creation timestamp           |

---

# SQL Setup Script

### Create Database
```sql
CREATE DATABASE student_db;
