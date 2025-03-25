# To-Do List Application

## Overview
This is a full-stack To-Do List application built using **FastAPI** with MongoDB as the database. The app supports user authentication, task management, and task completion tracking.

## Features
✅ User authentication (signup, login, logout)  
✅ Token-based authentication (JWT)  
✅ Add, update, delete, and mark tasks as completed  
✅ MongoDB database for storing users and tasks  
✅ FastAPI for backend API  
 

---

## Tech Stack
### Backend
- **FastAPI** (Python-based API framework)
- **MongoDB** (Database)
- **JWT** (Authentication)
  
---

## Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/todo-list.git
cd todo-list
```

### 2️⃣ Backend Setup (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
> Backend runs on `http://localhost:8000`

---

## API Endpoints (Backend)

### Authentication
- `POST /auth/signup` → Create a new user
- `POST /auth/login` → User login (returns JWT token)

### To-Do Management
- `GET /todos` → Get all tasks
- `POST /todos` → Create a new task
- `PUT /todos/{id}/complete` → Mark a task as completed
- `DELETE /todos/{id}` → Delete a task

---

## Contributing
Feel free to fork this repository and submit pull requests! 🚀

---



## Contact
For questions or support, reach out to 
yogalingam.nithurzan@gmail.com

