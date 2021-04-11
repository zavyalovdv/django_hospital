from django.urls import path
from hospital.settings import *
from .views import *
from .authentification import user_login, user_logout


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('patients/', PatientsList.as_view(), name='patients'),
    path('patient/<int:pk>/', PatientDetail.as_view(), name='patient'),
    path('patient/edit/<int:pk>/', PatientUpdate.as_view(), name='patient_edit'),
    path('patient/add', PatientCreate.as_view(), name='add_patient'),
    path('doctors/', DoctorsList.as_view(), name='doctors'),
    path('doctor/<int:pk>/', DoctorDetail.as_view(), name='doctor'),
    path('departments/', DepartmentsList.as_view(), name='departments'),
    path('department/<int:pk>/', DepartmentDetail.as_view(), name='department'),
    path('wards/', WardsList.as_view(), name='wards'),
    path('ward/<int:pk>/', WardDetail.as_view(), name='ward'),
    path('history/<int:pk>/', HistoryDetail.as_view(), name='history'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
