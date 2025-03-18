from django.urls import path

from . import views


urlpatterns = [
    # ex: api/
    path("students/", views._student_all),
    path("students/<int:pk>", views._update_stud),
    path("staff/", views._staff_all),
    path("staff/<int:pk>", views._update_staf),
    path("clear/", views.clear_all),
]
