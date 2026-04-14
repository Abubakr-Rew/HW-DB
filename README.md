# ORM Backend Project (SQLAlchemy + SQLite)

## 📌 Description
This project is a simple backend system built using SQLAlchemy ORM and SQLite.

It demonstrates how to model relational databases and work with:
- One-to-One relationships
- One-to-Many relationships
- Many-to-Many relationships
- CRUD operations
- Basic queries with relationships

---

## 🧱 Project Structure

- User → Profile (1:1)
- User → Posts (1:N)
- Posts ↔ Tags (N:N)

---

## 🗃️ Models

### User
- id
- username (unique, not null)

### Profile
- id
- bio
- user_id (unique → 1:1)

### Post
- id
- title
- user_id (foreign key)

### Tag
- id
- name (unique)

### post_tag (association table)
- post_id
- tag_id

---

## 🔗 Relationships

- One-to-One: User ↔ Profile  
- One-to-Many: User → Posts  
- Many-to-Many: Posts ↔ Tags  

---

## ⚙️ Features

### CRUD (User)
- Create user
- Read user by ID
- Read user by username
- Update user
- Delete user

---

### 🔍 Queries
- Get user by ID
- Get user by username
- Get all posts of a user
- Get all posts by tag

---

## 📊 Demo Data

The project automatically creates sample data:
- Users: john, alice
- Profiles for each user
- Posts for users
- Tags: python, life

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install sqlalchemy