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
            return render(request,"movie.html",{"movie": movie})
# Create your views here.
