from django.urls import path
from hospital.settings import *
from .views import *

urlpatterns = [
    path('', HomeHospital.as_view(), name='home'),
    path('patients/', PatientsList.as_view(), name='patients'),
    path('patient/<int:pk>/', PatientDetail.as_view(), name='patient'),
    path('patient/edit/<int:pk>/', PatientUpdate.as_view(), name='patient_edit'),
    path('patient/add', PatientCreate.as_view(), name='add_patient'),
    path('doctors/', DoctorsList.as_view(), name='doctors'),
    path('doctor/<int:pk>/', show_doctor, name='doctor'),
    path('departments/', DepartmentsList.as_view(), name='departments'),
    path('department/<int:pk>/', show_department, name='department'),
    path('wards/', WardsList.as_view(), name='wards'),
    path('ward/<int:pk>/', show_ward, name='ward'),
    path('history/<int:pk>/', HistoryDetail.as_view(), name='history'),
]
