# Generated by Django 5.1.6 on 2025-04-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0003_alter_employees_employees_dateof_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='Employees_vacationleave_balance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
