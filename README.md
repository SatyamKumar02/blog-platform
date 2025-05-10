blog-platform/
├── django_project/
│   ├── blog/                 # Django app: Posts, Comments, Likes, Tags
│   ├── users/                # Django app: User profiles, authentication
│   ├── notifications/        # Django app: Notifications
│   ├── analytics/            # Django app: Usage tracking (optional)
│   ├── templates/            # Jinja-style HTML templates
│   │   ├── blog/
│   │   ├── users/
│   │   ├── notifications/
│   │   └── base.html
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── config/               # Django’s core configuration: settings, URLs, WSGI,ASGI
│   │   ├── __init__.py
│   │   ├── mongo_config.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── asgi.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── manage.py             # Django command-line utility
│
├── flask_service/
│   ├── app.py                    # Flask app file
│   ├── admin_panel/
│   │   ├── __init__.py
│   │   ├── views.py  
│   ├── upload_service/
│   │   ├── __init__.py
│   │   ├── routes.py             # Flask API endpoints for image uploads
│   │   └── utils/                # Image processing functions
│   │        └── image_utils.py   # image resizing/optimization logic
│   ├── analytics_service/
│   │   ├── __init__.py
│   │   └── routes.py             # /analytics endpoint
│   ├── static/uploads/           # Store uploaded images temporarily
│   ├── templates/
│   │   └── admin
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml            # For Docker (Django + Flask + MongoDB + Redis)
├── README.md
└── .env                         # Environment variables (DB credentials, secret keys)

=============================================
User --> Django (Main App) --> MongoDB (Main Database)
                           --> Flask Microservice --> MongoDB (or temporary Redis)
=============================================

✅ Topics You Will Cover
Django Models, Admin, Forms, Views, Templates
Django Class-based Views (CBVs)
MongoDB integration (Djongo/MongoEngine)
Flask REST API microservice
Celery for background processing
Django Authentication + Permissions
Signals, Middlewares, Context Processors
Django REST Framework (for API)
Docker deployment
Real-time Communication with WebSockets (optional)

==============================================

 docker compose build --no-cache


my django admin panel - http://localhost:8000/admin/
root1, satyamksingh02@gmail.com, 12345678

=================================================
inside django container
\blog-platform> docker run -it --rm -v ${PWD}/django_project:/app blog-django bash
    1  django-admin startproject config .
    2  ls
    3  rm -rf /app/*
    4  ls
    5  django-admin startproject config .
    6  ls
    7  python manage.py runserver 0.0.0.0:8000
    8  python manage.py migrate
    9  python manage.py createsuperuser
   10  python manage.py runserver 0.0.0.0:8000
   11  history
   12  python manage.py startapp users
   13  python manage.py startapp blog
   14  python manage.py startapp notifications
   15  python manage.py startapp analytics
   16  python manage.py runserver 0.0.0.0:8000
   17  python manage.py makemigrations
   18  python manage.py makemigrations
   19  pip install Pillow
   20  python manage.py makemigrations
   21  python manage.py migrate
   22  python manage.py runserver 0.0.0.0:8000
   23  python manage.py makemigrations
   24  python manage.py migrate
   25  python manage.py runserver 0.0.0.0:8000
   26  history