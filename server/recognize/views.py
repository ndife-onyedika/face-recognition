import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from django.shortcuts import render, reverse
from django.views.decorators.csrf import csrf_exempt
from .serializers import STUDENT_SERIALIZERS, STAFF_SERIALIZERS
from .api_serializers import API_STUDENT_SERIALIZERS, API_STAFF_SERIALIZERS
from .details.recognize import _recog_stud, _recog_staf
from users.models import STUDENTS, STAFF
from django.conf import settings as django_settings


# create views
@api_view(["POST"])
@csrf_exempt
def _verify_stud(request):
    students = STUDENTS.objects.all()

    serializer = STUDENT_SERIALIZERS(students, many=True, context={"request": request})

    if request.method == "POST":
        image_file = request.FILES["image"]

        count = -1
        for student in students:
            count += 1

            image_processed = _recog_stud(student, image_file)

            if image_processed == serializer.data[count]["id"]:
                return Response(serializer.data[count])
            else:
                return HttpResponse(image_processed)


@api_view(["POST"])
@csrf_exempt
def _verify_staff(request):
    staff = STAFF.objects.all()

    serializer = STAFF_SERIALIZERS(staff, many=True, context={"request": request})

    if request.method == "POST":
        image_file = request.FILES["image"]

        count = -1
        for staf in staff:
            count += 1

            image_processed = _recog_staf(staf, image_file)

            if image_processed == serializer.data[count]["id"]:
                return Response(serializer.data[count])
            else:
                return HttpResponse(image_processed)


@api_view(["POST"])
@csrf_exempt
def api_verify_stud(request):
    students = STUDENTS.objects.all()

    serializer = API_STUDENT_SERIALIZERS(students, many=True, context={"request": request})

    if request.method == "POST":
        image_file = request.FILES["image"]

        count = -1
        for student in students:
            count += 1

            image_processed = _recog_stud(student, image_file)

            if image_processed == serializer.data[count]["id"]:
                staf = serializer.data[count]
                return Response(serializer.data[count])
            else:
                return HttpResponse(image_processed)


@api_view(["POST"])
@csrf_exempt
def api_verify_staff(request):
    staff = STAFF.objects.all()

    serializer = API_STAFF_SERIALIZERS(staff, many=True, context={"request": request})

    if request.method == "POST":
        image_file = request.FILES["image"]

        count = -1
        for staf in staff:
            count += 1

            image_processed = _recog_staf(staf, image_file)

            if image_processed == serializer.data[count]["id"]:
                return Response(serializer.data[count])
            else:
                return HttpResponse(image_processed)


def show_full_details_student(request):
    if request.method == "GET":
        pdf = f"{django_settings.MEDIA_ME}pdf/student_detail.pdf"
        response = HttpResponse(open(pdf, "rb").read(), content_type="application/pdf")
        return response


def show_full_details_staff(request):
    if request.method == "GET":
        pdf = f"{django_settings.MEDIA_ME}pdf/staff_detail.pdf"
        response = HttpResponse(open(pdf, "rb").read(), content_type="application/pdf")
        return response
