
# Django Movies App

A simple Django application that displays a list of movies and allows the user to view details for each movie.

## Movies

The movies are stored in memory as a Python list:

- Inception
- The Dark Knight
- Interstellar

Each movie has:

- ID
- Title
- Year
- Rating

---

# MVT Architecture

Django uses the **MVT (Model - View - Template)** architecture.

```text
                 USER / BROWSER
                       |
                       | HTTP Request
                       v
                +--------------+
                |     URL      |
                |   urls.py    |
                +--------------+
                       |
                       | matches URL
                       v
                +--------------+
                |     VIEW     |
                |   views.py   |
                +--------------+
                       |
             +---------+---------+
             |                   |
             | get movie data    |
             v                   |
        +------------+           |
        |   MODEL    |           |
        |   models   |           |
        +------------+           |
             |                   |
             +---------+---------+
                       |
                       | context/data
                       v
                +--------------+
                |   TEMPLATE   |
                |    HTML      |
                +--------------+
                       |
                       | HTML Response
                       v
                 USER / BROWSER
````

## MVT Flow in This Project

```text
Browser
   |
   | GET /
   v
urls.py
   |
   | index
   v
views.py
   |
   | movies list
   v
index.html
   |
   | displays movies
   v
Browser
```

For a movie detail page:

```text
Browser
   |
   | GET /1/
   v
urls.py
   |
   | movie_detail(1)
   v
views.py
   |
   | find movie with id = 1
   v
movie.html
   |
   | display movie details
   v
Browser
```

---

# Project Structure

```text
mysite/
│
├── manage.py
│
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── movies/
    ├── views.py
    ├── urls.py
    │
    └── templates/
        ├── index.html
        └── movie.html
```

---

# Views

`movies/views.py`

```python
from django.shortcuts import render

movies = [
    {
        "id": 1,
        "title": "Inception",
        "year": 2010,
        "rating": 8.8
    },
    {
        "id": 2,
        "title": "The Dark Knight",
        "year": 2008,
        "rating": 9.0
    },
    {
        "id": 3,
        "title": "Interstellar",
        "year": 2014,
        "rating": 8.7
    }
]


def index(request):
    return render(request, "index.html", {"movies": movies})


def movie_detail(request, movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return render(
                request,
                "movie.html",
                {"movie": movie}
            )
```

---

# URLs

`movies/urls.py`

```python
from django.urls import path
from .views import index, movie_detail

urlpatterns = [
    path("", index, name="index"),
    path("<int:movie_id>/", movie_detail, name="movie_detail"),
]
```

In the main `mysite/urls.py`:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("movies/", include("movies.urls")),
]
```

---

# Templates

## index.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Movies</title>
</head>
<body>

<h1>Movies</h1>

{% for movie in movies %}

    <h2>{{ movie.title }}</h2>

    <p>Year: {{ movie.year }}</p>

    <p>Rating: {{ movie.rating }}</p>

    <a href="{% url 'movie_detail' movie.id %}">
        View Details
    </a>

    <hr>

{% endfor %}

</body>
</html>
```

## movie.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ movie.title }}</title>
</head>
<body>

<h1>{{ movie.title }}</h1>

<p>Year: {{ movie.year }}</p>

<p>Rating: {{ movie.rating }}</p>

<a href="{% url 'index' %}">
    Back to Movies
</a>

</body>
</html>
```

---

# URLs

Movie list:

```text
http://127.0.0.1:8000/movies/
```

Inception:

```text
http://127.0.0.1:8000/movies/1/
```

The Dark Knight:

```text
http://127.0.0.1:8000/movies/2/
```

Interstellar:

```text
http://127.0.0.1:8000/movies/3/
```

---

# How to Run

Activate the virtual environment:

```bash
source venv/bin/activate
```

Run the Django server:

```bash
python3 manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/movies/
```

---

# MVT Summary

| Part         | Django File        | Responsibility             |
| ------------ | ------------------ | -------------------------- |
| **Model**    | `models.py`        | Handles data/database      |
| **View**     | `views.py`         | Handles logic and requests |
| **Template** | `templates/*.html` | Displays HTML              |
| **URL**      | `urls.py`          | Connects URLs to views     |

### Simple way to remember

```text
URL → VIEW → DATA → TEMPLATE → USER
```

In this project:

```text
/movies/1/
     ↓
movie_detail()
     ↓
movies list
     ↓
movie.html
     ↓
Movie details
```
