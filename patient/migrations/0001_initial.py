# Generated by Django 3.0.8 on 2021-03-31 20:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Отделение')),
            ],
            options={
                'verbose_name': 'Отделение',
                'verbose_name_plural': 'Отделения',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=100, verbose_name='Отчество')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('experience', models.PositiveSmallIntegerField(verbose_name='Стаж')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='department_to_doctor', to='patient.Department', verbose_name='Отделение')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
                'ordering': ['surname'],
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(help_text='В формате - 010', max_length=3, unique=True, validators=[django.core.validators.RegexValidator(message='Упс... Попробуйте снова', regex='^[0-9]{3}$')], verbose_name='Номер палаты')),
                ('phone', models.CharField(help_text='В формате - 0010', max_length=4, unique=True, validators=[django.core.validators.RegexValidator(message='Упс... Попробуйте снова', regex='^[0-9]{4}$')], verbose_name='Номер телефона палаты')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patient.Department', verbose_name='Закрепленное отделение')),
            ],
            options={
                'verbose_name': 'Палата',
                'verbose_name_plural': 'Палаты',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_security_number', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]{6}$')], verbose_name='Номер страхового полиса')),
                ('surname', models.CharField(blank=True, max_length=100, verbose_name='Фамилия')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Имя')),
                ('second_name', models.CharField(blank=True, max_length=100, verbose_name='Отчество')),
                ('sex', models.CharField(choices=[('неизвестно', 'Неизвестно'), ('мужской', 'Мужской'), ('женский', 'Женский'), ('неприменимо', 'Неприменимо')], max_length=15, verbose_name='Пол')),
                ('pre_age', models.CharField(choices=[('менее 10', 'менее 10'), ('от 10 до 25', 'от 10 до 25'), ('от 25 до 45', 'от 25 до 45'), ('от 25 до 45', 'от 45 до 65'), ('от 65 и более', 'от 65 и более')], max_length=15, verbose_name='Примерный возраст в годах')),
                ('height', models.CharField(choices=[('менее 170', 'менее 170'), ('от 170 до 185', 'от 170 до 185'), ('от 185 и боле', 'от 185 и более')], max_length=15, verbose_name='Примерный рост, (см)')),
                ('hair_color', models.CharField(choices=[('черные', 'Черные'), ('русые', 'Русые'), ('светлые', 'Светлые'), ('седые', 'Седые'), ('красные', 'Красные'), ('оранжевые', 'Оранжевые'), ('желтые', 'Желтые'), ('зеленые', 'Зеленые'), ('синие', 'Синие'), ('фиолетовые', 'Фиолетовые'), ('розовые', 'Розовые'), ('разноцветные', 'Разноцветные'), ('нет волос', 'Нет волос')], max_length=15, verbose_name='Цвет волос')),
                ('special_signs', models.CharField(max_length=255, verbose_name='Особые приметы')),
                ('admitted_hospital_date', models.DateTimeField(verbose_name='Дата и время поступления в больницу')),
                ('severity_disease', models.CharField(choices=[('критическое', 'Критическое'), ('Тяжелое', 'Тяжелое'), ('средней тяжести', 'Средней тяжести'), ('среднее', 'Среднее'), ('хорошее', 'Хорошее')], max_length=15, verbose_name='Текущее состояние')),
                ('provisional_diagnosis', models.CharField(max_length=255, verbose_name='Предварительный диагноз')),
                ('medical_history', models.TextField(blank=True, verbose_name='История болезни')),
                ('change_ward_date', models.DateTimeField(verbose_name='Дата назнечения в палату')),
                ('current_status', models.CharField(choices=[('в палате', 'В палате'), ('на операции', 'На операции'), ('на процедурах', 'На процедурах'), ('на приеме у врача', 'На приеме у врача'), ('неизвестно', 'Неизвестно')], max_length=30, verbose_name='Текущий статус')),
                ('how_admitted', models.CharField(choices=[('направлен из поликлиники', 'Направлен из поликлиники'), ('доставлен на скорой помощи', 'Доставлен на скорой помощи'), ('обратился самостоятельно', 'Обратился самостоятельно'), ('другое', 'Другое')], max_length=30, verbose_name='Способ обращения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания профиля')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Последняя дата редактирования')),
                ('is_discharged', models.BooleanField(default=False, verbose_name='Пациент выписан')),
                ('discharged_hospital_date', models.DateField(blank=True, null=True, verbose_name='Дата выписки из больницы')),
                ('cause_discharged', models.CharField(blank=True, max_length=100, verbose_name='Основание для выписки')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='department_to_patient', to='patient.Department', verbose_name='Отделение')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='patient_to_doctor', to='patient.Doctor', verbose_name='Лечаший врач')),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ward_number_to_patient', to='patient.Ward', verbose_name='Номер палаты')),
            ],
            options={
                'verbose_name': 'карточку пациента',
                'verbose_name_plural': 'Карточки пациентов',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='MovementHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_ward_number', models.CharField(help_text='В формате - 010', max_length=4, unique=True, validators=[django.core.validators.RegexValidator(message='Упс... Попробуйте снова', regex='^[0-9]{3}$')], verbose_name='Текущаяя палата')),
                ('next_ward_number', models.CharField(help_text='В формате - 010', max_length=3, unique=True, validators=[django.core.validators.RegexValidator(message='Упс... Попробуйте снова', regex='^[0-9]{3}$')], verbose_name='Номер будущей палаты')),
                ('ward_movement_date', models.DateTimeField(auto_now=True, verbose_name='Дата перемещения')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patient.Patient', verbose_name='Пациент')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalPatient',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('social_security_number', models.CharField(db_index=True, max_length=12, validators=[django.core.validators.RegexValidator(regex='^[0-9]{6}$')], verbose_name='Номер страхового полиса')),
                ('surname', models.CharField(blank=True, max_length=100, verbose_name='Фамилия')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Имя')),
                ('second_name', models.CharField(blank=True, max_length=100, verbose_name='Отчество')),
                ('sex', models.CharField(choices=[('неизвестно', 'Неизвестно'), ('мужской', 'Мужской'), ('женский', 'Женский'), ('неприменимо', 'Неприменимо')], max_length=15, verbose_name='Пол')),
                ('pre_age', models.CharField(choices=[('менее 10', 'менее 10'), ('от 10 до 25', 'от 10 до 25'), ('от 25 до 45', 'от 25 до 45'), ('от 25 до 45', 'от 45 до 65'), ('от 65 и более', 'от 65 и более')], max_length=15, verbose_name='Примерный возраст в годах')),
                ('height', models.CharField(choices=[('менее 170', 'менее 170'), ('от 170 до 185', 'от 170 до 185'), ('от 185 и боле', 'от 185 и более')], max_length=15, verbose_name='Примерный рост, (см)')),
                ('hair_color', models.CharField(choices=[('черные', 'Черные'), ('русые', 'Русые'), ('светлые', 'Светлые'), ('седые', 'Седые'), ('красные', 'Красные'), ('оранжевые', 'Оранжевые'), ('желтые', 'Желтые'), ('зеленые', 'Зеленые'), ('синие', 'Синие'), ('фиолетовые', 'Фиолетовые'), ('розовые', 'Розовые'), ('разноцветные', 'Разноцветные'), ('нет волос', 'Нет волос')], max_length=15, verbose_name='Цвет волос')),
                ('special_signs', models.CharField(max_length=255, verbose_name='Особые приметы')),
                ('admitted_hospital_date', models.DateTimeField(verbose_name='Дата и время поступления в больницу')),
                ('severity_disease', models.CharField(choices=[('критическое', 'Критическое'), ('Тяжелое', 'Тяжелое'), ('средней тяжести', 'Средней тяжести'), ('среднее', 'Среднее'), ('хорошее', 'Хорошее')], max_length=15, verbose_name='Текущее состояние')),
                ('provisional_diagnosis', models.CharField(max_length=255, verbose_name='Предварительный диагноз')),
                ('medical_history', models.TextField(blank=True, verbose_name='История болезни')),
                ('change_ward_date', models.DateTimeField(verbose_name='Дата назнечения в палату')),
                ('current_status', models.CharField(choices=[('в палате', 'В палате'), ('на операции', 'На операции'), ('на процедурах', 'На процедурах'), ('на приеме у врача', 'На приеме у врача'), ('неизвестно', 'Неизвестно')], max_length=30, verbose_name='Текущий статус')),
                ('how_admitted', models.CharField(choices=[('направлен из поликлиники', 'Направлен из поликлиники'), ('доставлен на скорой помощи', 'Доставлен на скорой помощи'), ('обратился самостоятельно', 'Обратился самостоятельно'), ('другое', 'Другое')], max_length=30, verbose_name='Способ обращения')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Дата создания профиля')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Последняя дата редактирования')),
                ('is_discharged', models.BooleanField(default=False, verbose_name='Пациент выписан')),
                ('discharged_hospital_date', models.DateField(blank=True, null=True, verbose_name='Дата выписки из больницы')),
                ('cause_discharged', models.CharField(blank=True, max_length=100, verbose_name='Основание для выписки')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('department', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='patient.Department', verbose_name='Отделение')),
                ('doctor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='patient.Doctor', verbose_name='Лечаший врач')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('ward', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='patient.Ward', verbose_name='Номер палаты')),
            ],
            options={
                'verbose_name': 'historical карточку пациента',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
