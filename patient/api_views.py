from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import PatientsListSerializers


class APIPatientsListView(APIView):
    def get(self, request):
        patients = Patient.objects.filter(is_discharged=False)
        serializer = PatientsListSerializers(patients, many=True)
        return Response(serializer.data)
