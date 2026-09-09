from django.shortcuts import render

from django.core.paginator import Paginator
courses = [

    {
        "id": 1,
        "name": "Python",
        "description": "Learn Python programming basics",
        "category": "programming",
        "difficulty": "beginner",
    },

    {
        "id": 2,
        "name": "Django",
        "description": "Build web applications with Django",
        "category": "web",
        "difficulty": "intermediate",
    },

    {
        "id": 3,
        "name": "JavaScript",
        "description": "Learn JavaScript for web development",
        "category": "programming",
        "difficulty": "beginner",
    },

    {
        "id": 4,
        "name": "React",
        "description": "Build modern user interfaces with React",
        "category": "web",
        "difficulty": "intermediate",
    },

    {
        "id": 5,
        "name": "HTML & CSS",
        "description": "Learn the fundamentals of building web pages",
        "category": "web",
        "difficulty": "beginner",
    },

    {
        "id": 6,
        "name": "Java",
        "description": "Learn object-oriented programming with Java",
        "category": "programming",
        "difficulty": "intermediate",
    },

    {
        "id": 7,
        "name": "SQL",
        "description": "Learn how to work with databases and write SQL queries",
        "category": "database",
        "difficulty": "beginner",
    },

    {
        "id": 8,
        "name": "PostgreSQL",
        "description": "Learn advanced database concepts using PostgreSQL",
        "category": "database",
        "difficulty": "advanced",
    },

    {
        "id": 9,
        "name": "UI/UX Design",
        "description": "Learn the basics of designing user-friendly interfaces",
        "category": "design",
        "difficulty": "beginner",
    },

    {
        "id": 10,
        "name": "Figma",
        "description": "Create professional UI designs and prototypes with Figma",
        "category": "design",
        "difficulty": "beginner",
    },

    {
        "id": 11,
        "name": "Machine Learning",
        "description": "Learn the fundamentals of machine learning",
        "category": "ai",
        "difficulty": "advanced",
    },

    {
        "id": 12,
        "name": "Data Science",
        "description": "Analyze data using Python and popular data science tools",
        "category": "data",
        "difficulty": "intermediate",
    },

    {
        "id": 13,
        "name": "Node.js",
        "description": "Build backend applications using JavaScript and Node.js",
        "category": "backend",
        "difficulty": "intermediate",
    },

    {
        "id": 14,
        "name": "Git & GitHub",
        "description": "Learn version control and collaboration with Git and GitHub",
        "category": "tools",
        "difficulty": "beginner",
    },

    {
        "id": 15,
        "name": "Cybersecurity",
        "description": "Learn the fundamentals of cybersecurity and online security",
        "category": "security",
        "difficulty": "advanced",
    },

]

def course_list(request):
    category = request.GET.get("category", "all")
    difficulty = request.GET.get("difficulty", "all")
    search = request.GET.get("search", "")

    filtered_courses = courses

    if category != "all":
        filtered_courses = [
            course for course in filtered_courses
            if course.get("category") == category
        ]

    if difficulty != "all":
        filtered_courses = [
            course for course in filtered_courses
            if course.get("difficulty") == difficulty
        ]

    if search:
        filtered_courses = [
            course for course in filtered_courses
            if search.lower() in course.get("name", "").lower()
        ]

    paginator = Paginator(filtered_courses, 2)

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "courses.html",
        {
            "courses": page_obj,
            "page_obj": page_obj,
        },
    )
    
    
def course_detail(request, id):
    for course in courses:
        if course["id"] == id:
            tab = request.GET.get("tab", "details")

            return render(
                request,
                "course_detail.html",
                {
                    "course": course,
                    "tab": tab,
                },
            )

    return render(request)