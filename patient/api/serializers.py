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


class DoctorDetailSerializer(serializers.ModelSerializer):
    doctor = serializers.SlugRelatedField(slug_field='surname', read_only=True)

    class Meta:
        model = Doctor
        exclude = ''


class DepartmentsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class DepartmentDetailSerializer(serializers.ModelSerializer):
    depatment = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Department
        exclude = ''


class WardsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ward
        fields = '__all__'


class WardDetailSerializer(serializers.ModelSerializer):
    ward = serializers.SlugRelatedField(slug_field='number', read_only=True)

    class Meta:
        model = Ward
        exclude = ''
