import os
import cv2
import numpy as np
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from django.shortcuts import render, reverse
from django.views.decorators.csrf import csrf_exempt
from .serializers import STUDENT_SERIALIZERS, STAFF_SERIALIZERS
from django.conf import settings as django_settings
from users.models import STUDENTS, STAFF

# Create your views here.
@api_view(["POST", "GET"])
@csrf_exempt
def _register_student(request):
    if request.method == "POST":
        student = STUDENTS.objects.create(
            first_name=request.POST.get("first_name"),
            middle_name=request.POST.get("middle_name"),
            last_name=request.POST.get("last_name"),
            date_of_birth=request.POST.get("date_of_birth"),
            age=request.POST.get("age"),
            gender=request.POST.get("gender"),
            nationality=request.POST.get("nationality"),
            state_of_origin=request.POST.get("state_of_origin"),
            lga_origin=request.POST.get("lga_origin"),
            marital_status=request.POST.get("marital_status"),
            jamb_number=request.POST.get("jamb_number"),
            college=request.POST.get("college"),
            department=request.POST.get("department"),
            level=request.POST.get("level"),
            matric_number=request.POST.get("matric_number"),
            address=request.POST.get("address"),
            phone_number=request.POST.get("phone_number"),
            email=request.POST.get("email"),
            parent_name=request.POST.get("parent_name"),
            parent_email=request.POST.get("parent_email"),
            parent_phone=request.POST.get("parent_phone"),
            date_of_registration=request.POST.get("date_of_registration"),
            pic="aa",
        )
        return HttpResponse("Student Profile Created!!")
    elif request.method == "GET":
        student = STUDENTS.objects.all()

        serializer = STUDENT_SERIALIZERS(
            student, many=True, context={"request": request}
        )

        return Response(serializer.data[-1])


@api_view(["POST"])
def _update_student(request, pk):
    if request.method == "POST":
        try:
            file = request.FILES["image"]
        except BaseException:
            return HttpResponse("No file uploaded!")
        else:
            student = STUDENTS.objects.get(pk=pk)

            image = cv2.imdecode(
                np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED
            )

            cv2.imwrite(
                f"{django_settings.MEDIA_ME}image/student/{student.last_name}_{student.first_name}/{student.last_name}_{student.first_name}.jpg".lower(),
                image,
            )

            student.pic = f"image/student/{student.last_name}_{student.first_name}/{student.last_name}_{student.first_name}.jpg".lower()

            student.save()

        return HttpResponse("Student Profile Updated!")


@api_view(["POST", "GET"])
@csrf_exempt
def _register_staff(request):
    if request.method == "POST":
        staff = STAFF.objects.create(
            first_name=request.POST.get("first_name"),
            middle_name=request.POST.get("middle_name"),
            last_name=request.POST.get("last_name"),
            date_of_birth=request.POST.get("date_of_birth"),
            age=request.POST.get("age"),
            gender=request.POST.get("gender"),
            nationality=request.POST.get("nationality"),
            state_of_origin=request.POST.get("state_of_origin"),
            lga_origin=request.POST.get("lga_origin"),
            marital_status=request.POST.get("marital_status"),
            profession=request.POST.get("profession"),
            address=request.POST.get("address"),
            phone_number=request.POST.get("phone_number"),
            email=request.POST.get("email"),
            date_of_registration=request.POST.get("date_of_registration"),
            pic="aa",
        )

        return HttpResponse("Staff Profile Created!!")

    elif request.method == "GET":
        staff = STAFF.objects.all()
        serializer = STAFF_SERIALIZERS(staff, many=True, context={"request": request})

        return Response(serializer.data[-1])


@api_view(["POST"])
def _update_staff(request, pk):
    if request.method == "POST":
        staff = STAFF.objects.get(pk=pk)
        try:
            file = request.FILES["image"]
        except BaseException:
            return HttpResponse("No file uploaded!")
        else:
            image = cv2.imdecode(
                np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED
            )

            cv2.imwrite(
                f"{django_settings.MEDIA_ME}image/staff/{staff.last_name}_{staff.first_name}/{staff.last_name}_{staff.first_name}.jpg".lower(),
                image,
            )

            staff.pic = f"image/staff/{staff.last_name}_{staff.first_name}/{staff.last_name}_{staff.first_name}.jpg".lower()

            staff.save()

        return HttpResponse("Staff Profile Updated!")

