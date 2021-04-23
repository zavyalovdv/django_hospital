from django.urls import path
from .views import *


urlpatterns = [
    path('patients/', APIPatientsListView.as_view(), name='api_patients'),
    path('patient/<int:pk>/', APIPatientDetailView.as_view(), name='api_patient'),
    path('doctors/', APIDoctorsListView.as_view(), name='api_doctors'),
    path('doctor/<int:pk>', APIDoctorDetailView.as_view(), name='api_doctor'),
    path('departments/', APIDepartmentsListView.as_view(), name='api_departments'),
    path('department/<int:pk>', APIDepartmentDetailView.as_view(), name='api_department'),
    path('wards/', APIWardsListView.as_view(), name='api_wards'),
    path('ward/<int:pk>/', APIWardDetailView.as_view(), name='api_ward'),
    path('create-patient/', APIPatientsListView.as_view(), name='api_create_patient'),
]