from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.course_list, name="list"),
    path("category/<str:name>/", views.category, name="category"),
    path("<slug:slug>/", views.course_detail, name="detail"),
]