from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, DeleteView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.dispatch import receiver
from django.contrib.auth.mixins import LoginRequiredMixin

from patient.models import *
from .forms import PatientForm, UserLoginForm


class HomePage(ListView):
    template_name = 'patient/home/home.html'

    #Required method
    def get_queryset(self):
        return HttpResponse('')


class PatientsList(LoginRequiredMixin ,ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Patient
    template_name = 'patient/patient/patients_list.html'
    extra_context = {
        'title': 'Список пациентов',
    }
    allow_empty = False
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PatientsList, self).get_context_data(**kwargs)
        history = Patient.history.all()
        context['title'] = 'Список пациентов'
        return context

    def get_queryset(self):
        return Patient.objects.filter(is_discharged=False)


class PatientDetail(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient/patient_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = Patient.objects.get(pk=self.kwargs['pk'])
        movement = MovementHistory.objects.filter(patient=self.kwargs['pk'])

        if patient.ward != patient.was_ward:
            print(f'Ward: {patient.ward}, Was ward: {patient.was_ward}')
        context['patient'] = patient
        context['movement'] = movement
        return context


class PatientUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient/patient_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PatientCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient/add_patient.html'


class DoctorsList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Doctor
    template_name = 'patient/doctor/doctors_list.html'
    extra_context = {
        'title': 'Список врачей',
    }
    allow_empty = False


class DepartmentsList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Department
    template_name = 'patient/department/departments_list.html'
    extra_context = {
        'title': 'Список отделений',
    }
    allow_empty = False


class WardsList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Ward
    template_name = 'patient/ward/wards_list.html'
    extra_context = {
        'title': 'Список палат',
    }
    allow_empty = False


class DoctorDetail(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Doctor
    template_name = 'patient/doctor/doctor.html'
    context_object_name = 'doctor'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = Patient.objects.filter(doctor=self.kwargs['pk'])
        context['patient'] = patient
        return context


class DepartmentDetail(LoginRequiredMixin, DetailView):
    model = Department
    template_name = 'patient/department/department.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        doctor = Doctor.objects.filter(department=self.kwargs['pk'])
        patient = Patient.objects.filter(department=self.kwargs['pk'])
        context['patient'] = patient
        context['doctor'] = doctor
        return context


class WardDetail(LoginRequiredMixin, DetailView):
    model = Ward
    template_name = 'patient/ward/ward.html'
    context_object_name = 'ward'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = Patient.objects.filter(ward=self.kwargs['pk'])
        context['patient'] = patient
        return context


class HistoryDetail(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Patient
    template_name = 'patient/history/history.html'
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient_history = MovementHistory.objects.filter(patient=self.kwargs['pk'])
        context['patient_history'] = patient_history
        return context
