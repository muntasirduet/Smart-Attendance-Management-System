# Smart Attendance Management System

A Django-based web application for managing student attendance in an academic institution. The system supports three user roles — **Student**, **Teacher**, and **Sub-Admin** — and provides face-recognition-assisted attendance tracking powered by OpenCV.

![Landing Page](https://github.com/akashbis/Smart-Attendance-Management-System/assets/31843024/d3c453ac-89f2-428b-b527-ebeaa8f02015)

---

## Features

- **Landing page** with separate login portals for students and teachers.
- **Student portal** – register, log in, view enrolled courses, and check personal attendance records.
- **Teacher portal** – register, log in, manage courses, enrol students, take attendance manually or via webcam (OpenCV face capture), and view attendance reports.
- **Sub-Admin (Admin) portal** – manage classes/courses, assign teachers, and administer the system.
- **Face-recognition attendance** – webcam integration via OpenCV for automated attendance capture.
- SQLite database (development); easily swappable for PostgreSQL or MySQL in production.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.7 · Django 3.2 |
| Computer Vision | OpenCV (`opencv-python-headless`) · NumPy |
| Frontend | HTML / CSS / JavaScript (Jinja2 templates) |
| Database | SQLite (default) |
| Auth | Django built-in auth (`django.contrib.auth`) |

---

## Project Structure

```
smartApp/               # Django project root
├── manage.py
├── db.sqlite3
├── smartApp/           # Project settings, URLs, WSGI/ASGI
│   ├── settings.py
│   └── urls.py
├── student/            # Student app (models, views, URLs)
├── teacher/            # Teacher app (models, views, face recognition)
├── subadmin/           # Sub-Admin app (class/course management)
├── templates/          # Shared HTML templates
│   ├── landing.html
│   ├── student/
│   ├── teacher/
│   └── admin/
└── static/             # Static assets (CSS, JS, images)
    └── saved-media/    # Uploaded / captured media (git-ignored)
```

---

## Data Models

### Student (`student` app)
| Field | Type |
|---|---|
| user | OneToOne → `auth.User` |
| student_id | CharField |
| first_name / last_name | CharField |
| department | CharField |
| year / semester / section | CharField |

### Teacher (`teacher` app)
| Field | Type |
|---|---|
| user | OneToOne → `auth.User` |
| first_name / last_name | CharField |
| phone_number | CharField |
| dept / faculty / designation | CharField |

### Course
Links students (`student_code`) to subjects (`subject_code`).

### AttendanceDB
Stores per-student, per-course daily attendance records (`status`, `comment`, `at_date`).

### Class (`subadmin` app)
Defines a course with `course_code`, `course_name`, assigned `course_teacher`, `department`, `year`, and `semester`.

### SubAdmin (`subadmin` app)
Administrative user linked to `auth.User`.

---

## Getting Started

### Prerequisites

- Python 3.7+
- pip
- A webcam (optional — only required for face-recognition attendance)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/muntasirduet/Smart-Attendance-Management-System.git
cd Smart-Attendance-Management-System

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install django==3.2 opencv-python-headless numpy django-webcam

# 4. Navigate to the Django project root
cd smartApp

# 5. Apply database migrations
python manage.py migrate

# 6. Create a Django superuser (for the admin panel)
python manage.py createsuperuser

# 7. Start the development server
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser.

---

## Usage

### URL Structure

| URL prefix | Portal |
|---|---|
| `/` | Landing page (choose Student or Teacher login) |
| `/student/` | Student portal |
| `/teacher/` | Teacher portal |
| `/subadmin/` | Sub-Admin portal |
| `/admin/` | Django built-in admin panel |

### Typical Workflow

1. **Sub-Admin** logs in → creates classes (course code, name, teacher, department, year, semester).
2. **Teacher** registers → logs in → selects a class → enrols students by year/semester/department.
3. **Teacher** takes attendance:
   - *Manual*: marks each student present/absent with an optional comment.
   - *Auto (webcam)*: activates the camera; press **q** to finish capture.
4. **Student** logs in → views enrolled courses and personal attendance history.

---

## Configuration

Key settings in `smartApp/smartApp/settings.py`:

| Setting | Default | Notes |
|---|---|---|
| `DEBUG` | `True` | Set to `False` in production |
| `SECRET_KEY` | insecure dev key | **Change before deploying** |
| `ALLOWED_HOSTS` | `[]` | Add your domain/IP for production |
| `DATABASES` | SQLite | Replace with PostgreSQL/MySQL for production |

---

## Saved Media

Images captured during attendance are stored in `smartApp/static/saved-media/`. This directory is excluded from version control (see its `readme.md`). Training images used for face recognition should be placed in a sibling `images/` directory.

---

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m "Add your feature"`.
4. Push and open a Pull Request.

---

## License

This project is open source. Please check with the repository owner for licensing details before use in production.
