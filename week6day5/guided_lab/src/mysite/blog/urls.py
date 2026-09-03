from django.urls import path
from .views import list, detail

app_name = "blog"

urlpatterns = [
    path("", list, name="list"),
    path("<int:id>/", detail, name="detail"),
]