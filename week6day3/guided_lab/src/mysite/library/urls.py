from .views import books_list, index,book_detail
from django.urls import path

urlpatterns = [
    path("", index, name="index"),
    path("<int:book_id>/", book_detail, name="book_detail")
]