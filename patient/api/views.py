from rest_framework.response import Response
from rest_framework.views import APIView

from patient.models import *
from .serializers import *


class APIPatientsListView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientsListSerializer(patients, many=True)
        return Response({'patient': serializer.data})

    def post(self, request):
        patient = request.data.get('patient')
        serializer = PatientsListSerializer(data=patient)
        if serializer.is_valid(raise_exception=True):
            patient_saved = serializer.save()
            return Response({'success': 'Patient created'})
        else:
            return Response(data='WRONG', status=500)


class APIPatientDetailView(APIView):
    def get(self, request, pk):
        patient = Patient.objects.get(pk=pk, is_discharged=False)
        serializer = PatientDetailSerializer(patient)
        return Response(serializer.data)


class APIDoctorsListView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorsListSerializer(doctors, many=True)
        return Response(serializer.data)


class APIDoctorDetailView(APIView):
    def get(self, request, pk):
        doctor = Doctor.objects.get(pk=pk)
        serializer = DoctorDetailSerializer(doctor)
        return Response(serializer.data)


class APIDepartmentsListView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentsListSerializer(departments, many=True)
        return Response(serializer.data)


class APIDepartmentDetailView(APIView):
    def get(self, request, pk):
        department = Department.objects.get(pk=pk)
        serializer = DepartmentDetailSerializer(department)
        return Response(serializer.data)


class APIWardsListView(APIView):
    def get(self, request):
        wards = Ward.objects.all()
        serializer = WardsListSerializer(wards, many=True)
        return Response(serializer.data)


class APIWardDetailView(APIView):
    def get(self, request, pk):
        ward = Ward.objects.get(pk=pk)
        serializer = WardDetailSerializer(ward)
        return Response(serializer.data)


class APICreatePatientView(APIView):
    def get(self, request):
        return Response(status=200, data='POST Only')

    def post(self, request):
        serializer = Pa(data=request.data)
        print("SERIALIZER: ", serializer)
        print("DATA: ",request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(status=500)
