# 🚀 Production-Ready Flask Authentication API

A production-ready REST API built with Flask that provides user registration, authentication, and secure password handling.

---

## 🔧 Features

* User registration
* Secure password hashing
* Login system
* RESTful API design
* Clean architecture (models, resources, separation of concerns)

---

## 🛠 Tech Stack

* Python
* Flask
* Flask-RESTful
* SQLAlchemy
* Werkzeug (password hashing)

---

## 📂 Project Structure

```
.
├── api.py
├── models.py
├── create_db.py
├── resources/
│   ├── user.py
│   ├── users.py
│   └── login.py
├── requirements.txt
```

---

## ▶️ Getting Started

### 1. Clone repository

```bash
git clone https://github.com/Patrick95-creator/production-flask-api.git
cd production-flask-api
```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the server

```bash
python api.py
```

Server runs on:

```
http://127.0.0.1:5000
```

---

## 🔐 API Endpoints

### ➕ Register User

POST `/api/users`

```json
{
  "name": "Patrick",
  "email": "test@test.com",
  "password": "1234"
}
```

---

### 🔑 Login

POST `/api/login`

```json
{
  "email": "test@test.com",
  "password": "1234"
}
```

---

## 🧠 What I Learned

* Building REST APIs with Flask
* Structuring backend projects professionally
* Password hashing and authentication
* Working with databases using SQLAlchemy
* Using Git & GitHub in a real project

---

## 📌 Future Improvements

* JWT Authentication
* Docker support
* Deployment (AWS / Render)
* Input validation improvements

---

## 👤 Author

Patrick S.
