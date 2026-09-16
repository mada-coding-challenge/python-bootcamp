from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("add/<int:product_id>/",views.add_product,name="add_product" ),
    path("clear-cart/", views.clear_cart,name="clear_cart"),
    path("theme/<str:theme>/", views.set_theme, name="set_theme"),
]