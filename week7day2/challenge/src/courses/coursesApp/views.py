from django.http import Http404
from django.shortcuts import render


courses = [
    {
        "name": "Python Fundamentals",
        "level": "Beginner",
        "student_count": 120,
        "description": "Learn Python programming from the basics and build a strong foundation.",
        "image": "python.jpg",
    },
    {
        "name": "Django Web Development",
        "level": "Intermediate",
        "student_count": 85,
        "description": "Learn how to build modern web applications using Django.",
        "image": "django.jpg",
    },
    {
        "name": "HTML & CSS",
        "level": "Beginner",
        "student_count": 200,
        "description": "<script>alert('Learn HTML and CSS to create beautiful web pages.');</script>",
        "image": "html-css.jpg",
    },
    {
        "name": "JavaScript",
        "level": "Intermediate",
        "student_count": 150,
        "description": "Learn JavaScript and create interactive web applications.",
        "image": "javascript.jpg",
    },
]


def home(request):
    return render(request, "coursesApp/home.html")


def course_list(request):
    return render(
        request,
        "coursesApp/courses.html",
        {"courses": courses},
    )


def course_detail(request, course_name):

    for course in courses:
        if course["name"].lower() == course_name.lower():

            return render(
                request,
                "coursesApp/course_detail.html",
                {
                    "name": course["name"],
                    "level": course["level"],
                    "student_count": course["student_count"],
                    "description": course["description"],
                    "image": course["image"],
                }
            )
