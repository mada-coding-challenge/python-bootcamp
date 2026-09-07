from django.urls import path
from . import views


app_name = "courses"


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("list/", views.course_list, name="list"),
]