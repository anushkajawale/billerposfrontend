# Generated by Django 5.1.6 on 2025-04-02 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roles', '0003_remove_roles_roles_id_roles_billwiseprofit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
