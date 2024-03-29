# Generated by Django 3.0.8 on 2021-04-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_auto_20210406_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpatient',
            name='admitted_hospital_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время поступления в больницу'),
        ),
        migrations.AlterField(
            model_name='historicalpatient',
            name='severity_disease',
            field=models.CharField(blank=True, choices=[('критическое', 'Критическое'), ('Тяжелое', 'Тяжелое'), ('средней тяжести', 'Средней тяжести'), ('среднее', 'Среднее'), ('хорошее', 'Хорошее')], max_length=15, null=True, verbose_name='Текущее состояние'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='admitted_hospital_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время поступления в больницу'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='severity_disease',
            field=models.CharField(blank=True, choices=[('критическое', 'Критическое'), ('Тяжелое', 'Тяжелое'), ('средней тяжести', 'Средней тяжести'), ('среднее', 'Среднее'), ('хорошее', 'Хорошее')], max_length=15, null=True, verbose_name='Текущее состояние'),
        ),
    ]
