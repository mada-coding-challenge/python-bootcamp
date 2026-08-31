from .views import index
from .views import faq
from .views import team
from django.urls import path

urlpatterns = [
    path("", index, name="index"),
    path("faq/", faq, name="faq"),
    path("team/", team, name="team"),
]