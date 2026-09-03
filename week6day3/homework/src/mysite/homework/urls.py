from django.contrib import admin
from django.urls import path
from .views import create_view, details_view

urlpatterns = [
    path("admin/", admin.site.urls),

    path("products/create/", create_view),

    path("products/id/<str:id>/", details_view),
]