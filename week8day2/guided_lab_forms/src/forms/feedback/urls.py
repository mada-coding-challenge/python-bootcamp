from django.urls import path
from .views import feedback, thank_you

urlpatterns = [
    path("", feedback, name="feedback"),
    path("thank-you/", thank_you, name="thank_you"),
]