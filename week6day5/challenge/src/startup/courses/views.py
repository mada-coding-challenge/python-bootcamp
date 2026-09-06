from django.shortcuts import render


courses = [
    {
        "title": "Python Basics",
        "slug": "python-basics",
        "description": "Learn the basics of Python.",
        "category": "Programming",
    },
    {
        "title": "Django",
        "slug": "django",
        "description": "Learn how to build websites with Django.",
        "category": "Web Development",
    },
    {
        "title": "HTML & CSS",
        "slug": "html-css",
        "description": "Learn the basics of HTML and CSS.",
        "category": "Web Development",
    },
]


def course_list(request):
    return render(request, "courses/list.html", {"courses": courses})


def course_detail(request, slug):
    for course in courses:
        if course["slug"] == slug:
            return render(
                request,
                "courses/detail.html",
                {"course": course}
            )

    return render(request, "404.html", status=404)


def category(request, name):
    filtered_courses = []

    for course in courses:
        if course["category"].lower() == name.lower():
            filtered_courses.append(course)

    return render(
        request,
        "courses/category.html",
        {
            "courses": filtered_courses,
            "category": name,
        }
    )