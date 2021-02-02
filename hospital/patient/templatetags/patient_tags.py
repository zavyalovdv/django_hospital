from django import template
from patient.models import *

register = template.Library()


@register.simple_tag()
def get_patients():
    return Patient.objects.all()


@register.simple_tag()
def get_doctors():
    return Doctor.objects.all()


@register.simple_tag()
def get_departments():
    return Department.objects.all()


@register.simple_tag()
def get_wards():
    return Ward.objects.all()

