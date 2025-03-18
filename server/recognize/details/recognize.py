import cv2
import numpy as np
import os
import json

from django.conf import settings as django_settings
import face_recognition
from .create_pdf import _create_stud_pdf, _create_staf_pdf


def _recog_stud(student, image):

    img = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    known_face_encodings = []
    known_face_id = []

    known_id = student.id
    name = f"{student.last_name}_{student.first_name}".lower()

    for image in os.listdir(f"{django_settings.MEDIA_ME}image/student/{name}"):
        _image = face_recognition.load_image_file(
            f"{django_settings.MEDIA_ME}image/student/{name}/{image}"
        )
        _image_face_encoding = face_recognition.face_encodings(_image)[0]

        # Create arrays of known face encodings and their ids
        known_face_encodings.append(_image_face_encoding)
        known_face_id.append(known_id)

    # img = cv2.resize(in_img, (0, 0), fx=0.25, fy=0.25)

    unknown_image = img[:, :, ::-1]
    # unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    if face_locations == []:
        return "Unable to find face"
    else:
        for (top, right, bottom, left), face_encoding in zip(
            face_locations, face_encodings
        ):

            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding
            )

            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding
            )

            _id = None

            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                _id = known_face_id[best_match_index]

                if student.id == _id:
                    _create_stud_pdf(student)
                    return student.id
            else:
                return "Unknown Individual"


def _recog_staf(staff, image):

    img = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    known_face_encodings = []
    known_face_id = []

    known_id = staff.id
    name = f"{staff.last_name}_{staff.first_name}".lower()

    for image in os.listdir(f"{django_settings.MEDIA_ME}image/staff/{name}"):
        _image = face_recognition.load_image_file(
            f"{django_settings.MEDIA_ME}image/staff/{name}/{image}"
        )
        _image_face_encoding = face_recognition.face_encodings(_image)[0]

        # Create arrays of known face encodings and their ids
        known_face_encodings.append(_image_face_encoding)
        known_face_id.append(known_id)

    # img = cv2.resize(in_img, (0, 0), fx=0.25, fy=0.25)

    unknown_image = img[:, :, ::-1]
    # unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    if face_locations == []:
        return "Unable to find face"
    else:
        for (top, right, bottom, left), face_encoding in zip(
            face_locations, face_encodings
        ):

            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding
            )

            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding
            )

            _id = None

            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                _id = known_face_id[best_match_index]

                if staff.id == _id:
                    _create_staf_pdf(staff)
                    return staff.id
            else:
                return "Unknown Individual"
