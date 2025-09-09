# FastAPI Todo App

A simple FastAPI project with JWT authentication and CRUD for todos using MySQL.

---

## 🚀 Setup Guide

### 1. Clone Repo
```bash
git clone https://github.com/nilesh297/fastapi-todo.git
cd fastapi-todo

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate   # Linux/Mac

3. Install Dependencies
pip install -r requirements.txt

4. Configure .env
Create a .env file in the root:
DB_USER=root
DB_PASS=your_mysql_password
DB_HOST=localhost
DB_NAME=fastapi_todo
JWT_SECRET=supersecret

5. Setup Database
CREATE DATABASE fastapi_todo;

6. Run App
uvicorn app.main:app --reload



🧪 Testing

Signup
POST /auth/signup
{
  "name": "Nilesh",
  "email": "nilesh@example.com",
  "password": "12345"
}

Login
POST /auth/login
{
  "email": "nilesh@example.com",
  "password": "12345"
}

Use the returned access_token as a Bearer Token for /todos/ routes.

Save → commit → push:
```cmd
git add README.md
git commit -m "Added README setup guide"
git push


3. Export Postman Collection

In Postman, create requests for:

Signup (POST /auth/signup)

Login (POST /auth/login)

Create Todo (POST /todos/)

Get Todos (GET /todos/)

Update (PUT /todos/{id})

Delete (DELETE /todos/{id})

Save them to a Collection.

Click the 3 dots → Export → Collection v2.1.

Save as FastAPI-Todo.postman_collection.json inside your project root.
