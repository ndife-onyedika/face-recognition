from django.urls import path

from . import views


urlpatterns = [
    # ex: api/
    path("student/", views._verify_stud),
    path("staff/", views._verify_staff),
    path("d_stud/", views.show_full_details_student),
    path("d_staf/", views.show_full_details_staff),
]
