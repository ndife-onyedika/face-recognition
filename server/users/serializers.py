from rest_framework import serializers
from users.models import STUDENTS, STAFF


class STUDENT_SERIALIZERS(serializers.ModelSerializer):
    class Meta:
        model = STUDENTS
        fields = "__all__"


class STAFF_SERIALIZERS(serializers.ModelSerializer):
    class Meta:
        model = STAFF
        fields = "__all__"
