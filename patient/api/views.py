from rest_framework.response import Response
from rest_framework.views import APIView

from patient.models import *
from .serializers import PatientsListSerializer, PatientDetailSerializer, DoctorsListSerializer


class APIPatientsListView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientsListSerializer(patients, many=True)
        return Response(serializer.data)

class APIPatientDetailView(APIView):
    def get(self, request, pk):
        patient = Patient.objects.get(id=pk, is_discharged=False)
        serializer = PatientDetailSerializer(patient)
        return Response(serializer.data)


class APIDoctorsListView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorsListSerializer(doctors, many=True)
        return Response(serializer.data)
