from rest_framework import serializers

from patient.models import *


class PatientsListSerializer(serializers.ModelSerializer):

    # social_security_number = serializers.CharField()
    # surname = serializers.CharField()
    # name = serializers.CharField()
    # second_name = serializers.CharField()
    # sex = serializers.CharField()
    # pre_age = serializers.CharField()
    # height = serializers.CharField()
    # hair_color = serializers.CharField()
    # special_signs = serializers.CharField()
    # admitted_hospital_date = serializers.DateTimeField()
    # severity_disease = serializers.CharField()
    # provisional_diagnosis = serializers.CharField()
    # medical_history = serializers.CharField()
    # department = serializers.IntegerField()
    # doctor = serializers.IntegerField()
    # ward = serializers.IntegerField()
    # change_ward_date = serializers.DateTimeField()
    # current_status = serializers.CharField()
    # how_admitted = serializers.CharField()
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    # is_discharged = serializers.BooleanField()
    # discharged_hospital_date = serializers.DateField()
    # cause_discharged = serializers.CharField()
    # movement_date = serializers.DateTimeField()

    # def create(self, validated_data):
    #     return Patient.objects.create(**validated_data)

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


class PatientCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, validation_data):
        patient = Patient.objects.create(
            social_security_number = validation_data.get('social_security_number', None),
            surname = validation_data.get('social_security_number', None),
            name = validation_data.get('social_security_number', None),
            second_name = validation_data.get('social_security_number', None),
            sex = validation_data.get('social_security_number', None),
            pre_age = validation_data.get('social_security_number', None),
            height = validation_data.get('social_security_number', None),
            hair_color = validation_data.get('social_security_number', None),
            special_signs = validation_data.get('social_security_number', None),
            admitted_hospital_date = validation_data.get('social_security_number', None),
            severity_disease = validation_data.get('social_security_number', None),
            provisional_diagnosis = validation_data.get('social_security_number', None),
            medical_history = validation_data.get('social_security_number', None),
            department = validation_data.get('social_security_number', None),
            doctor = validation_data.get('social_security_number', None),
            ward = validation_data.get('social_security_number', None),
            change_ward_date = validation_data.get('social_security_number', None),
            current_status = validation_data.get('social_security_number', None),
            how_admitted = validation_data.get('social_security_number', None),
            created_at = validation_data.get('social_security_number', None),
            updated_at = validation_data.get('social_security_number', None),
            is_discharged = validation_data.get('social_security_number', None),
            discharged_hospital_date = validation_data.get('social_security_number', None),
            cause_discharged = validation_data.get('social_security_number', None),
            movement_date = validation_data.get('social_security_number', None),
            history = validation_data.get('social_security_number', None),)

        return patient


# {"social_security_number": "000555", "surname":"testapi", "name":"testapi", "second_name": "testapi", "sex": "Мужской", "pre_age": "от 10 до 25", "height": "менее 170", "hair_color": "Черные", "special_signs": "no", "admitted_hospital_date": "06.04.1993", "severity_disease": "Тяжелое", "provisional_diagnosis": "testapi", "medical_history": "testapi", "department": "Терапия", "doctor": "Широкова Алиса Артёмовна", "ward": "0010", "change_ward_date": "06.04.1993", "current_status": "В палате", "how_admitted": "Направлен из поликлиники", "created_at": "06.04.1993", "updated_at": "06.04.1993", "is_discharged": "False", "discharged_hospital_date":"06.04.1993", "cause_discharged":"No", "movement_date":"06.04.1993", "history":""}


# {
#     "patient": {
#         "social_security_number": "000555",
#         "surname":"testapi",
#         "name":"testapi",
#         "second_name": "testapi",
#         "sex": "Мужской",
#         "pre_age": "от 10 до 25",
#         "height": "менее 170",
#         "hair_color": "Черные", 
#         "special_signs": "no",
#         "severity_disease": "Тяжелое",
#         "provisional_diagnosis": "testapi",
#         "medical_history": "testapi",
#         "department": "Терапия",
#         "doctor": "Широкова Алиса Артёмовна",
#         "ward": "0010",
#         "current_status": "В палате",
#         "how_admitted": "Направлен из поликлиники",
#         "is_discharged": "False",
#         "discharged_hospital_date":"06.04.1993",
#         "cause_discharged":"No"
#     }
# }


# {
#     "patient": {
#         "social_security_number": "000555",
#         "surname":"testapi",
#         "name":"testapi",
#         "second_name": "testapi",
#         "sex": "Мужской",
#         "pre_age": "от 10 до 25",
#         "height": "менее 170",
#         "hair_color": "Черные", 
#         "special_signs": "no",
#         "admitted_hospital_date":"2021-04-06 19:25:00+00",
#         "severity_disease": "Тяжелое",
#         "provisional_diagnosis": "testapi",
#         "medical_history": "testapi",
#         "department": 2,
#         "doctor": 6,
#         "ward": 3,
#         "change_ward_date": "2021-04-06 19:25:00+00",
#         "current_status": "В палате",
#         "how_admitted": "Направлен из поликлиники",
#         "created_at": "2021-04-06 19:25:00+00",
#         "updated_at": "2021-04-06 19:25:00+00",
#         "is_discharged": "False",
#         "discharged_hospital_date":"2021-04-06",
#         "cause_discharged":"No",
#         "movement_date":"2021-04-06 19:25:00+00"
#     }
# }