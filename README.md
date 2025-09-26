# 🎮 FastAPI Flutter API Integration
A simple frontend-backend project that exposes a FastAPI REST API back-end and a Flutter frontend to showcase API integration, Pydantic Schemas, Alembic Migrations and SQLAlchemy ORM models.

## ✳️ Visual Overview 

https://github.com/user-attachments/assets/f1a26771-ae05-4d54-a23e-2f703f18c8f3


## 📹 Demo
First, see it in action:
1. Open a terminal and start the backend.
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
2. - In Postman, set the base_url to `localhost:8000`, the headers to `Content-Type`:`application/json` and send a POST /new with the body (below) to create a new fruit.

<img width="910" height="567" alt="FastAPI-Flutter-Postman-Screenshot 2025-09-26 161419" src="https://github.com/user-attachments/assets/bcdd071e-f7bb-4f83-87b6-bc50b221292e" />

```json
{
  "name": "Strawberry",
  "seedless": true
}
```
3. Run the Flutter app on an emulator or device.
4. Switch to the List tab to fetch and view fruits.



## 🔍 Project Overview

### Problem
- Provide a reliable HTTP API for managing fruit records and a simple cross-platform UI for users to view and add fruits.

### Key Components
- FastAPI REST endpoints
- SQLAlchemy ORM models
- Alembic migration scripts
- Pydantic schemas for input/output validation
- Flutter UI with bottom navigation
- Dart model mapping TINYINT seedless flag to bool
- HTTP integration tested via Postman


## 🛠️ Getting Started
1. Clone
```bash
git clone https://github.com/ex-rnd/FastAPI-Flutter-API-Integration-Using-Alembic-MySQL.git
cd fastapi-flutter-integration
```

2. Backend setup
- Create a Python virtual environment.
```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```
- Install requirements.
```bash
pip install -r requirements.txt
```

- Create a .env with your MySQL URL.
```bash
DATABASE_URL=mysql+pymysql://user:pass@host:3306/dbname
```
- Run alembic migrations.
```bash
alembic upgrade head
```

3. Frontend setup
- Navigate to the flutter folder.
```bash
cd frontend
```

- Fetch Dart packages.
```bash
flutter pub get
```

- Update lib/config.dart with your API base URL.
<img width="434" height="106" alt="Flutter-URL-For-Local-Host-Screenshot 2025-09-26 163016" src="https://github.com/user-attachments/assets/e7f24538-05bf-4ab6-b952-f391a80d828d" />


## ▶️ Usage
### API Testing with Postman.
- Open Postman.
- Use the Environment to set `base_url` to `http://127.0.0.1:8000`.

- Run requests and inspect responses.
- Use `GET, POST, PUT`.

- Automate tests by creating assertions on status codes and JSON schemas

### Flutter Front-End.
- Ensure your emulator or device is connected
- From project root:
```
cd frontend
flutter run
```


## 🚀 API Reference

<img width="1035" height="558" alt="FastAPI-Flutter-API-Reference-Screenshot 2025-09-26 164721" src="https://github.com/user-attachments/assets/d3aa0fe6-3733-4c0e-a31b-4670558d7976" />


## 📐 App Architecture
```md
Flutter App  ← HTTP (http package) →  FastAPI  
    ↑                                     │  
    │                                     ↓  
 ListView / Form             SQLAlchemy ORM → MySQL  
                             Alembic Migrations  
```
```md
[Flutter UI] → http.get/post → [FastAPI App]
  ↓                          ↓
ListView / Form      Pydantic validation
                      ↓
                 SQLAlchemy models
                      ↓
                  MySQL database
               (migrations via Alembic)  
```


## 🤝 Contributing
- Fork the repo
- Branch naming: feature/xyz or fix/xyz
- Run linters:
```bash
Backend: flake8, black
Frontend: flutter format
```
- Add tests:
```bash
Backend unit tests with: pytest
Frontend widget tests with: flutter test
```
- Submit PRs with clear descriptions and link related issues


### 🎮 Thank you for exploring FastAPI-Flutter integration 🎉!










