from django.shortcuts import render


def home(request):
    return render(request, "courses/home.html")


def about(request):
    return render(request, "courses/about.html")


def course_list(request):
    courses = [
        {
            "title": "Python Basics",
            "description": "Learn the basics of Python.",
            "category": "Programming",
        },
        {
            "title": "Django",
            "description": "Learn how to build websites with Django.",
            "category": "Web Development",
        },
        {
            "title": "HTML & CSS",
            "description": "Learn how to create and style web pages.",
            "category": "Frontend",
        },
    ]

    return render(
        request,
        "courses/list.html",
        {"courses": courses}
    )