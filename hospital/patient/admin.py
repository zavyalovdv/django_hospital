from django.contrib import admin
from .models import *


class PatientAdmin(admin.ModelAdmin):
    list_display = ('social_security_number', 'surname', 'name', 'second_name', 'current_status', 'ward',
                    'department', 'severity_disease', 'is_discharged')
    list_display_links = ('social_security_number', 'surname', 'name', 'second_name')
    search_fields = ('social_security_number', 'surname')
    list_editable = ('current_status', 'ward', 'severity_disease', 'is_discharged',)
    list_filter = ('current_status', 'ward', 'severity_disease', 'is_discharged',)


admin.site.register(Patient, PatientAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'second_name', 'surname',
                    'date_of_birth', 'experience',)


admin.site.register(Doctor, DoctorAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Department, DepartmentAdmin)


class WardAdmin(admin.ModelAdmin):
    list_display = ('number', 'phone',)


admin.site.register(Ward, WardAdmin)
