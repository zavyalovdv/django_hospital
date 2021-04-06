from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from patient.models import *
from .forms import PatientForm, UserLoginForm
from django.views.generic.edit import CreateView, UpdateView
from django.db.models.signals import pre_save
from django.views.generic import ListView, DetailView, DeleteView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.dispatch import receiver


class HomePage(ListView):
    template_name = 'patient/home/home.html'

    def get_queryset(self):
        return HttpResponse('')


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
        # ward = Ward.objects.get(self.get.number)
        history = Patient.history.all()
        context['title'] = 'Список пациентов'
        return context

    def get_queryset(self):
        return Patient.objects.filter(is_discharged=False)


class PatientDetail(DetailView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient/patient_detail.html'
    context_object_name = 'object'
    movement_uniq = {}
    movement_list = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = Patient.objects.get(pk=self.kwargs['pk'])
        movement = MovementHistory.objects.filter(patient=self.kwargs['pk'])

        if patient.ward != patient.was_ward:
            print(f'Ward: {patient.ward}, Was ward: {patient.was_ward}')
        context['patient'] = patient
        context['movement'] = movement
        return context


class PatientUpdate(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient/patient_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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


class HistoryDetail(DeleteView):
    model = Patient
    template_name = 'patient/history/history.html'
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient_history = MovementHistory.objects.filter(patient=self.kwargs['pk'])
        context['patient_history'] = patient_history
        return context

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request ,user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, template_name='patient/login/login.html', context={'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')