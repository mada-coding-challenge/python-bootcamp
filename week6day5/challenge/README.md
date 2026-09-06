# Startup Django Project

A Django project demonstrating multiple apps, URL namespaces, template inheritance, and **Class-Based Views (CBV)**.

## Project Apps

```text
startup/
├── users/
├── courses/
├── payment/
├── dashboard/
└── templates/
```

### Users

Handles user pages:

```text
/users/login/
/users/profile/
```

Uses CBV:

```python
class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")


class ProfileView(View):
    def get(self, request):
        return render(request, "users/profile.html")
```

### Courses

Handles:

```text
/courses/
/courses/python-basics/
/courses/category/programming/
```

Course details use a slug:

```python
path("<slug:slug>/", views.CourseDetailView.as_view(), name="detail")
```

### Payment

Handles:

```text
/payment/checkout/
/payment/receipt/
```

### Dashboard

Handles:

```text
/dashboard/
/dashboard/reports/
```

---

## Template Structure

```text
templates/
├── base.html
│
├── users/
│   ├── login.html
│   └── profile.html
│
├── courses/
│   ├── list.html
│   ├── detail.html
│   └── category.html
│
├── payment/
│   ├── checkout.html
│   └── receipt.html
│
└── dashboard/
    ├── home.html
    └── reports.html
```

All pages inherit from `base.html`:

```django
{% extends "base.html" %}
```

The common navigation and footer are therefore written only once.

---

## URL Namespaces

Each app has its own namespace.

### Users

```python
app_name = "users"
```

Use in templates:

```django
{% url 'users:login' %}
{% url 'users:profile' %}
```

### Courses

```python
app_name = "courses"
```

```django
{% url 'courses:list' %}
{% url 'courses:detail' course.slug %}
{% url 'courses:category' course.category %}
```

### Payment

```python
app_name = "payment"
```

```django
{% url 'payment:checkout' %}
{% url 'payment:receipt' %}
```

### Dashboard

```python
app_name = "dashboard"
```

```django
{% url 'dashboard:home' %}
{% url 'dashboard:reports' %}
```

---

## Class-Based Views

The `users` app uses CBVs.

Example:

```python
from django.views import View
from django.shortcuts import render


class LoginView(View):

    def get(self, request):
        return render(request, "users/login.html")
```

The URL uses `.as_view()`:

```python
path("login/", LoginView.as_view(), name="login")
```

### Why `.as_view()`?

It converts the class into a callable view that Django can use when a URL is requested.

```text
Browser
   ↓
URL
   ↓
LoginView.as_view()
   ↓
LoginView
   ↓
get()
   ↓
login.html
```

---

## Main URL Configuration

`startup/urls.py`:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("courses/", include("courses.urls")),
    path("payment/", include("payment.urls")),
    path("dashboard/", include("dashboard.urls")),
]
```

---

## Installation

Create and activate the virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install Django:

```bash
python3 -m pip install django
```

Run migrations:

```bash
python3 manage.py migrate
```

Start the development server:

```bash
python3 manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## MVT Flow

Django follows the **MVT pattern**:

```text
             Browser
                │
                ▼
              URL
                │
                ▼
              View
                │
          ┌─────┴─────┐
          │           │
          ▼           ▼
       Model       Template
          │           │
          └─────┬─────┘
                ▼
             Response
                │
                ▼
             Browser
```

In this project:

```text
URL
 ↓
users/urls.py
 ↓
LoginView
 ↓
login.html
 ↓
Browser
```

## Technologies

* Python
* Django
* HTML
* Django Templates
* Class-Based Views
* URL Namespaces
* Template Inheritance
* Slugs
