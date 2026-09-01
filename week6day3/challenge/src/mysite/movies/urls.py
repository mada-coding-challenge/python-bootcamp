from django.urls import path
from .views import index,movie_detail

urlpatterns = [
    path('', index, name="index"),
    path('<int:movie_id>/',movie_detail,name="movie_detail")
]