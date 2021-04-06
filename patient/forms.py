from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
import re


class PatientForm(forms.ModelForm):
    admitted_hospital_date = forms.DateTimeField(
        label='Дата поступления в больницу', input_formats=['%Y-%m-%dT%H:%M'], help_text='в формате d.m.Y, H:M',
        widget=forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'class': 'form-control', 'type': 'datetime-local'}))
    change_ward_date = forms.DateTimeField(
        label='Дата назначения в палату', input_formats=['%Y-%m-%dT%H:%M'], help_text='в формате d.m.Y, H:M',
        widget=forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'class': 'form-control', 'type': 'datetime-local'}))

    class Meta:
        model = Patient
        fields = [
            'social_security_number', 'surname', 'name', 'second_name', 'sex', 'pre_age', 'height', 'hair_color',
            'special_signs', 'admitted_hospital_date', 'severity_disease', 'provisional_diagnosis', 'medical_history',
            'department', 'doctor', 'ward', 'change_ward_date', 'current_status', 'how_admitted', 'is_discharged',
            'discharged_hospital_date', 'cause_discharged']
        widgets = {
            'social_security_number': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'second_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'pre_age': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.Select(attrs={'class': 'form-control'}),
            'hair_color': forms.Select(attrs={'class': 'form-control'}),
            'special_signs': forms.TextInput(attrs={'class': 'form-control'}),
            'admitted_hospital_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'severity_disease': forms.Select(attrs={'class': 'form-control'}),
            'provisional_diagnosis': forms.TextInput(attrs={'class': 'form-control'}),
            'medical_history': forms.Textarea(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'ward': forms.Select(attrs={'class': 'form-control'}),
            'change_ward_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'current_status': forms.Select(attrs={'class': 'form-control'}),
            'how_admitted': forms.Select(attrs={'class': 'form-control'}),
            'is_discharged': forms.CheckboxInput(attrs={'class': 'required checkbox'}),
            'discharged_hospital_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cause_discharged': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_surname(self):
        surname = self.cleaned_data['surname']
        if re.match(r'\d', surname):
            raise ValidationError('Фамилия не может начинаться с цифры')
        return surname

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
