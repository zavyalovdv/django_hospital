from rest_framework import serializers

from patient.models import *


class PatientsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'


class PatientDetailSerializer(serializers.ModelSerializer):

    patient = serializers.SlugRelatedField(slug_field='surname', read_only=True)

    class Meta:
        model = Patient
        exclude = ''


class DoctorsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'

