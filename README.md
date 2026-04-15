# 🎓 LearnX – Online Learning Platform (Django)

LearnX is a modern **online learning platform** built using Django where users can explore courses, watch videos, and track their learning progress.

---

## 🚀 Features

### 👤 Authentication

* User Registration & Login
* Secure authentication system
* Logout functionality

### 📚 Courses

* View all available courses
* Dynamic course listing from database
* Each course has:

  * Title
  * Description
  * Unique image

### 🎥 Course Detail

* View course content
* Watch video lectures
* Organized video structure

### 🧑‍💻 Admin Panel

* Add/Edit/Delete Courses
* Add videos for each course
* Upload course image via URL
* Manage platform content easily

### 🎨 UI Features

* Modern responsive design
* Animated backgrounds
* Glassmorphism UI
* Card-based layout

---

## 🏗️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS (Internal Styling)
* **Database:** SQLite (default)
* **Admin:** Django Admin Panel

---

## 📁 Project Structure

```
learnx/
│
├── accounts/        # Authentication (login/register)
├── courses/         # Courses & videos
├── templates/       # HTML templates
├── static/          # (optional)
├── manage.py
└── db.sqlite3
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/learnx.git
cd learnx
```

### 2️⃣ Create Virtual Environment

```
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser

```
python manage.py createsuperuser
```

### 6️⃣ Run Server

```
python manage.py runserver
```

---

## 🌐 Access URLs

* Home: http://127.0.0.1:8000/
* Courses: http://127.0.0.1:8000/courses/
* Admin: http://127.0.0.1:8000/admin/

---

## 🖼️ Adding Courses

1. Go to `/admin`
2. Add a new Course
3. Provide:

   * Title
   * Description
   * Image URL (from Unsplash)
4. Add Videos for that course

---

## 🔮 Future Enhancements

* 🔐 Enrollment system
* 📊 Progress tracking
* 🎥 Video player inside platform
* 📱 Mobile responsiveness improvements
* 🌍 Deployment (Render / AWS)

---

## 👨‍💻 Author

Developed by **E Naga Sai Revanth**

---

## ⭐ Support

If you like this project:

* ⭐ Star this repo
* 🍴 Fork it
* 📢 Share with others

---

## 📌 Note

This project is built for **learning purposes** and can be extended into a full production-level platform.

---

# 🚀 Happy Coding!
