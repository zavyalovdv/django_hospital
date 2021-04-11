from rest_framework import serializers

from .models import *


class PatientsListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'
