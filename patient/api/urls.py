from django.urls import path
from .api_views import *


urlpatterns = [
    path('patients/', APIPatientsListView.as_view(), name='api_patients'),
    path('patient/<int:pk>/', APIPatientDetailView.as_view(), name='api_patient'),
    path('doctors/', APIDoctorsListView.as_view(), name='api_doctors'),
]
