from django.shortcuts import render


blogs = [
    {
        "id": 1,
        "title": "My First Blog",
        "content": "This is my first blog post."
    },
    {
        "id": 2,
        "title": "Learning Django",
        "content": "Django makes web development easier."
    },
]


def list(request):
    return render(request, "list.html", {"blogs": blogs})


def detail(request, id):
    for blog in blogs:
        if blog["id"] == id:
            return render(request, "detail.html", {"blog": blog})
        
