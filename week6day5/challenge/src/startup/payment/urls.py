from django.urls import path
from .views import checkout, receipt

app_name = "payment"

urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("receipt/", receipt, name="receipt"),
]