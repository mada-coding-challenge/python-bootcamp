from django.urls import path
from . import views

app_name = "coursesApp"

urlpatterns = [
    path("", views.home, name="home"),
    path("courses/", views.course_list, name="courses"),
    path(
        "courses/<str:course_name>/",
        views.course_detail,
        name="course_detail",
    ),
]