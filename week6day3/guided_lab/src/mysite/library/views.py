from django.shortcuts import render
from django.http import JsonResponse

books = [
    {
        "id": 1,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "year": 1988
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    },
    {
        "id": 3,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937
    }
]


def books_list(request):
    return JsonResponse(books, safe=False)

# Create your views here.
# def books_detail(request, book_id):
#     book = None
#     for b in books:
#         if b["id"] == book_id:
#             book = b
#             break
#     if book:
#         return JsonResponse(book, safe=False)
    
def index(request):
    return render(request, "index.html", {"books": books})

def book_detail(request, book_id):
    book = None
    for b in books:
        if b["id"] == book_id:
            book = b
            break
    if book:
        return render(request, "book.html", {"book": book})