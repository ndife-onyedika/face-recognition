from django.urls import path

from . import views


urlpatterns = [
    # ex: api/
    path("students/", views._register_student),
    path("students/<int:pk>", views._update_student),
    path("staff/", views._register_staff),
    path("staff/<int:pk>", views._update_staff),
]
