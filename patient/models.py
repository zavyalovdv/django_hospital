from django.db import models
from .modelconst.MODELS_CONST import *
from django.core.validators import RegexValidator
from django.urls import reverse
from simple_history.models import HistoricalRecords
from django.utils import timezone


class MovementHistory(models.Model):
    prev_ward_number = models.CharField(verbose_name='Предыдущая палата', max_length=4, validators=[
        RegexValidator(regex='^[0-9]{3}$', message='Упс... Попробуйте снова')], help_text='В формате - 010', null=True)
    current_ward_number = models.CharField(verbose_name='Текущая палата', max_length=3, validators=[
        RegexValidator(regex='^[0-9]{3}$', message='Упс... Попробуйте снова')], help_text='В формате - 010', null=True)
    patient = models.ForeignKey('Patient', verbose_name='Пациент', on_delete=models.CASCADE, null=True)
    ward_movement_date = models.DateTimeField(verbose_name='Дата перемещения', null=True)

    def get_absolute_url(self):
        return reverse('movementhistory', kwargs={'pk': self.pk})


class Ward(models.Model):
    number = models.CharField('Номер палаты', max_length=3, unique=True, validators=[
        RegexValidator(regex='^[0-9]{3}$', message='Упс... Попробуйте снова')], help_text='В формате - 010')
    phone = models.CharField('Номер телефона палаты', max_length=4, unique=True, validators=[
        RegexValidator(regex='^[0-9]{4}$', message='Упс... Попробуйте снова')], help_text='В формате - 0010')
    department = models.ForeignKey('Department', verbose_name='Закрепленное отделение', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Палата'
        verbose_name_plural = 'Палаты'
        ordering = ['number']

    def get_absolute_url(self):
        return reverse('ward', kwargs={'pk': self.pk})

    def __str__(self):
        return self.number


class Department(models.Model):
    name = models.CharField('Отделение', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'

    def get_absolute_url(self):
        return reverse('department', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField('Имя', max_length=100, )
    second_name = models.CharField(
        'Отчество', max_length=100, )
    surname = models.CharField('Фамилия', max_length=100)
    date_of_birth = models.DateField('Дата рождения')
    experience = models.PositiveSmallIntegerField('Стаж')
    department = models.ForeignKey(
        Department, verbose_name='Отделение', on_delete=models.PROTECT, null=True, related_name='department_to_doctor')

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
        ordering = ['surname']

    def get_absolute_url(self):
        return reverse('doctor', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} {} {}'.format(self.surname, self.name, self.second_name)


class Patient(models.Model):
    social_security_number = models.CharField(
        'Номер страхового полиса', max_length=12, unique=True, validators=[RegexValidator(regex='^[0-9]{6}$')], )
    surname = models.CharField('Фамилия', max_length=100, blank=True)
    name = models.CharField('Имя', max_length=100, blank=True)
    second_name = models.CharField('Отчество', max_length=100, blank=True)
    sex = models.CharField('Пол', max_length=15, choices=SEX)
    pre_age = models.CharField('Примерный возраст в годах', max_length=15, choices=PRE_AGE)
    height = models.CharField('Примерный рост, (см)', max_length=15, choices=PRE_HEIGHT)
    hair_color = models.CharField('Цвет волос', max_length=15, choices=HAIR_COLOR)
    special_signs = models.CharField('Особые приметы', max_length=255, )
    admitted_hospital_date = models.DateTimeField('Дата и время поступления в больницу')
    severity_disease = models.CharField('Текущее состояние', max_length=15, choices=PATIENT_SEVERITY_DISEASE)
    provisional_diagnosis = models.CharField('Предварительный диагноз', max_length=255)
    medical_history = models.TextField('История болезни', blank=True)
    department = models.ForeignKey(
        Department, verbose_name='Отделение', on_delete=models.PROTECT, related_name='department_to_patient')
    doctor = models.ForeignKey(
        Doctor, verbose_name='Лечаший врач', on_delete=models.PROTECT, related_name='patient_to_doctor')
    ward = models.ForeignKey(
        Ward, verbose_name='Номер палаты', on_delete=models.PROTECT, related_name='ward_number_to_patient')
    change_ward_date = models.DateTimeField(verbose_name='Дата назнечения в палату')
    current_status = models.CharField('Текущий статус', max_length=30, choices=CURRENT_STATUS)
    how_admitted = models.CharField('Способ обращения', max_length=30, choices=HOW_ADMITTED)
    created_at = models.DateTimeField('Дата создания профиля', auto_now_add=True)
    updated_at = models.DateTimeField('Последняя дата редактирования', auto_now=True)
    is_discharged = models.BooleanField('Пациент выписан', default=False)
    discharged_hospital_date = models.DateField('Дата выписки из больницы', blank=True, null=True)
    cause_discharged = models.CharField('Основание для выписки', max_length=100, blank=True)
    movement_date = models.DateTimeField('Дата перемещения', blank=True, null=True)
    history = HistoricalRecords()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.was_ward = self.ward
        except Exception:
            pass

    class Meta:
        verbose_name = 'карточку пациента'
        verbose_name_plural = 'Карточки пациентов'
        ordering = ['-created_at']
    
    def get_absolute_url(self):
        return reverse('patient', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.surname} {self.name} {self.second_name}'

    def save(self, *args, **kwargs):
        try:
            if self.ward != self.was_ward:
                self.movement_date = timezone.now()
                MovementHistory.objects.create(prev_ward_number=self.was_ward, current_ward_number=self.ward,
                                               patient=self, ward_movement_date=self.movement_date)
        except Exception:
            pass
        return super().save(*args, **kwargs)
