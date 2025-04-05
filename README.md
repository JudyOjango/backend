# Threat Detection System – Backend

This repository contains the backend implementation of the **Threat Detection System**, a cybersecurity-focused application built using **Django** and **Django REST Framework**. It provides secure RESTful APIs for user authentication, threat detection processing, and system management.

---

## 🔧 Technologies Used

- Python 3.10+
- Django 5.2
- Django REST Framework
- Simple JWT for token-based authentication
- SQLite (default) / PostgreSQL (optional)
- CORS Headers for cross-origin communication

---

## Getting Started

Follow the steps below to set up and run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/JudyOjango/backend.git
cd backend
```

### 2. Set Up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv myenv
source myenv/bin/activate  # For Windows: myenv\Scripts\activate
```

### 3. Install Dependencies

Install all required packages using `pip`.

```bash
pip install -r requirements.txt
```

### 4. Configure Environment (Optional)

Ensure your `.env` or `settings.py` contains the correct configurations for:

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- Email credentials
- JWT settings

These are already partially configured in `settings.py`.

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

By default, the server will start on:  
 `http://127.0.0.1:8000`

---

## Project Structure

```
backend/
│
├── auth_app/           # Authentication logic and models
├── detection/          # Threat detection features
├── backend/            # Main project settings and URLs
├── templates/          # HTML templates (if any)
├── db.sqlite3          # Default database (SQLite)
└── manage.py           # Django project manager
```

---

## Deployment

The project is hosted on **Render** at:  
🔗 [https://backend-f1tj.onrender.com](https://backend-f1tj.onrender.com)

---

## Developer

**Judith Achieng' Ambogo**  
Cybersecurity and Software Engineering Enthusiast  
[GitHub Profile](https://github.com/JudyOjango)

---

## 📄 License

This project is licensed under MIT.

```
