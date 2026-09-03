# Django Blog Project

A simple Django project with multiple apps, template inheritance, namespaces, blog pages, and a custom 404 page.

## Project Structure

```text
src/
├── manage.py
│
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── pages/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── blog/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
└── templates/
    ├── base.html
    ├── home.html
    ├── about.html
    ├── contact.html
    ├── list.html
    ├── detail.html
    └── 404.html
```

## Features

* Home page
* About page
* Contact page
* Blog list
* Blog detail pages
* Custom 404 page
* Template inheritance using `base.html`
* URL namespaces
* In-memory blog data
* Django URL reversing with `{% url %}`

## URL Structure

```text
/                  → Home
/about/            → About
/contact/          → Contact

/blog/             → Blog list
/blog/1/           → Blog detail
/blog/2/           → Blog detail

/anything/         → Custom 404 page
```

## URL Namespaces

### Pages

`pages/urls.py`

```python
app_name = "pages"
```

URLs can then be used in templates:

```django
{% url 'pages:home' %}
{% url 'pages:about' %}
{% url 'pages:contact' %}
```

### Blog

`blog/urls.py`

```python
app_name = "blog"
```

Use:

```django
{% url 'blog:list' %}
{% url 'blog:detail' blog.id %}
```

## Template Inheritance

The project uses `base.html` as the main layout.

```html
{% extends "base.html" %}

{% block title %}About{% endblock %}

{% block content %}

<h1>About Us</h1>

<p>Welcome to our website.</p>

{% endblock %}
```

This allows all pages to share the same:

* Navigation
* Header
* Footer
* HTML structure

## Custom 404

In `mysite/urls.py`:

```python
handler404 = "pages.views.custom_404"
```

In `pages/views.py`:

```python
def custom_404(request, exception):
    return render(request, "404.html", status=404)
```

The `404.html` template extends `base.html`.

For testing the custom 404 page, set:

```python
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
```

## Templates Configuration

Because the `templates` folder is inside `src`, configure `settings.py`:

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        # ...
    },
]
```

## Run the Project

Activate the virtual environment:

```bash
source venv/bin/activate
```

Start Django:

```bash
python3 manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Main Django Flow

```text
Browser
   ↓
mysite/urls.py
   ↓
App urls.py
   ↓
View
   ↓
Context / Data
   ↓
Template
   ↓
HTML Response
   ↓
Browser
```

For example:

```text
/blog/1/
    ↓
mysite/urls.py
    ↓
blog/urls.py
    ↓
detail(request, id=1)
    ↓
Find blog
    ↓
detail.html
    ↓
Browser
```

## Technologies

* Python
* Django
* HTML
* Django Templates
* URL Namespaces
* Template Inheritance
