from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from patient.models import *
from .forms import PatientForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, DeleteView, FormView


class HomeHospital(ListView):
    template_name = 'patient/home/home.html'

    def get_queryset(self):
        return HttpResponse('<h1>User hello</h1>')


class PatientsList(ListView):
    model = Patient
    template_name = 'patient/patient/patients_list.html'
    extra_context = {
        'title': 'Список пациентов',
    }
    allow_empty = False
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PatientsList, self).get_context_data(**kwargs)
        context['title'] = 'Список пациентов'
        return context

    def get_queryset(self):
        return Patient.objects.filter(is_discharged=False)


class PatientDetail(DetailView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient/patient_detail.html'
    context_object_name = 'object'


# class PatientUpdate(UpdateView):
#     model = Patient
#     template_name = 'patient/patient/patient_detail.html'
#     fields = [
#         'social_security_number', 'surname', 'name', 'second_name', 'sex', 'pre_age', 'height', 'hair_color',
#         'special_signs', 'admitted_hospital_date', 'severity_disease', 'provisional_diagnosis', 'medical_history',
#         'department', 'doctor', 'ward', 'change_ward_date', 'current_status', 'how_admitted', 'is_discharged',
#         'discharged_hospital_date', 'cause_discharged']


class PatientDel(DeleteView):
    pass


class PatientCreate(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient/add_patient.html'


class DoctorsList(ListView):
    model = Doctor
    template_name = 'patient/doctor/doctors_list.html'
    extra_context = {
        'title': 'Список врачей',
    }
    allow_empty = False


class DepartmentsList(ListView):
    model = Department
    template_name = 'patient/department/departments_list.html'
    extra_context = {
        'title': 'Список отделений',
    }
    allow_empty = False


class WardsList(ListView):
    model = Ward
    template_name = 'patient/ward/wards_list.html'
    extra_context = {
        'title': 'Список палат',
    }
    allow_empty = False


# def show_patients(request):
#     context = {
#         'title': 'Пациенты',
#     }
#     return render(request, template_name='patient/patient/patients_list.html', context=context)


# def show_patient(request, pk):
#     patient = Patient.objects.get(pk=pk)
#     context = {
#         'patient': patient,
#         'title': 'Пациент: ',
#     }
#     return render(request, template_name='patient/patient/patient_detail.html', context=context)


# def show_doctors(request):
#     context = {
#         'title': 'Врачи',
#     }
#     return render(request, template_name='patient/doctor/doctors.html', context=context)


def show_doctor(request, pk):
    patient = Patient.objects.filter(doctor_id=pk)
    doctor = Doctor.objects.get(pk=pk)
    context = {
        'doctor': doctor,
        'title': 'Пациент',
        'patient': patient,
    }
    return render(request, template_name='patient/doctor/doctor.html', context=context)


# def show_departments(request):
#     context = {
#     }
#     return render(request, template_name='patient/department/departments.html', context=context)

def show_movement_history(request, pk):
    patient = Patient.objects.filter(ward_id=pk)
    ward = Ward.objects.filter(ward_id=pk)
    ward_movement_date = MovementHistory.ward_movement_date(ward_id=pk)
    context = {
        'title': 'Перемещения',
        'patient': patient,
        'ward': ward,
        'ward_movement_date': ward_movement_date,
    }
    return render(request, template_name='www.www', context=context)


def show_department(request, pk):
    doctor = Doctor.objects.filter(department_id=pk)
    patient = Patient.objects.filter(department_id=pk)
    department = Department.objects.get(pk=pk)
    context = {
        'title': 'Отделения',
        'department': department,
        'doctor': doctor,
        'patient': patient,
    }
    return render(request, template_name='patient/department/department.html', context=context)


# def show_wards(request):
#     context = {
#         'title': 'Палаты',
#     }
#     return render(request, template_name='patient/ward/wards.html', context=context)


def show_ward(request, pk):
    patient = Patient.objects.filter(ward_id=pk)
    ward = Ward.objects.get(pk=pk)
    context = {
        'title': 'Палаты',
        'ward': ward,
        'patient': patient,
    }
    return render(request, template_name='patient/ward/ward.html', context=context)


# def add_patient(request):
#     if request.method == 'POST':
#         form = PatientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('patients')
#     else:
#         form = PatientForm()
#     return render(request, 'patient/patient/add_patient.html', {'form': form, 'title': 'Новый пациент'})

