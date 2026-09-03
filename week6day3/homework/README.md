# Django URL Routing Homework

## 📚 Overview

This homework demonstrates how **Django URL routing** works when using a static URL and a dynamic URL parameter.

The main concept is understanding what happens when a URL such as:

```text
/products/create/
```

matches a specific URL pattern before a dynamic pattern such as:

```text
/products/<str:id>/
```

---

## 🎯 Objectives

* Create Django URL patterns.
* Create views for different URLs.
* Understand dynamic URL parameters.
* Understand URL pattern order.
* Understand why `"create"` can conflict with a dynamic `<str:id>`.
* Display the result in the browser.

---

## 📁 Project Structure

```text
project/
│
├── manage.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── products/
    ├── views.py
    ├── urls.py
    └── ...
```

---

## 🐍 `views.py`

```python
from django.http import HttpResponse


def create_view(request):
    return HttpResponse("CREATE VIEW")


def details_view(request, id):
    return HttpResponse(f"DETAILS VIEW - Product ID: {id}")
```

---

## 🔗 `urls.py`

```python
from django.urls import path
from .views import create_view, details_view

urlpatterns = [
    path("products/create/", create_view),

    path("products/id/<str:id>/", details_view),
]
```

---

## 🌐 Testing the URLs

### Create View

Visit:

```text
/products/create/
```

Result:

```text
CREATE VIEW
```

### Product with ID `"create"`

Visit:

```text
/products/id/create/
```

Result:

```text
DETAILS VIEW - Product ID: create
```

### Product with ID `"123"`

Visit:

```text
/products/id/123/
```

Result:

```text
DETAILS VIEW - Product ID: 123
```

---

## 🔄 URL Flow

```text
                Browser
                   │
                   ▼
        /products/create/
                   │
                   ▼
              urls.py
                   │
                   ▼
             create_view
                   │
                   ▼
            "CREATE VIEW"
```

And for a product:

```text
                Browser
                   │
                   ▼
        /products/id/create/
                   │
                   ▼
              urls.py
                   │
                   ▼
           details_view()
                   │
                   ▼
        id = "create"
                   │
                   ▼
  "DETAILS VIEW - Product ID: create"
```

---

## ⚠️ Important Concept

If you instead have:

```python
path("products/<str:id>/", details_view),
path("products/create/", create_view),
```

then:

```text
/products/create/
```

will match the dynamic route first.

Django checks URL patterns **from top to bottom**.

Therefore, specific URLs should generally come **before** dynamic URLs:

```python
path("products/create/", create_view),
path("products/<str:id>/", details_view),
```

This homework demonstrates how to avoid this type of URL conflict.
