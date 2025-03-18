from django.urls import path

from . import views


urlpatterns = [
    # ex: api/
    path("verify_student/", views.api_verify_stud),
    path("verify_staff/", views.api_verify_staff),
    path("d_stud/", views.show_full_details_student),
    path("d_staf/", views.show_full_details_staff),
]
