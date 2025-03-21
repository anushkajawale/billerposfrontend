# Generated by Django 5.1.6 on 2025-03-18 06:16

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('Roles_id', models.AutoField(primary_key=True, serialize=False)),
                ('Roles_name', models.CharField(max_length=255)),
                ('Roles_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='Roles_name', unique=True)),
            ],
            options={
                'db_table': 'tbl_Roles',
            },
        ),
    ]
