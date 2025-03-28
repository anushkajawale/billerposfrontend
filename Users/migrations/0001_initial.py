# Generated by Django 5.1.6 on 2025-03-19 15:39

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('users_id', models.AutoField(primary_key=True, serialize=False)),
                ('users_name', models.CharField(max_length=255)),
                ('users_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='users_name', unique=True)),
            ],
        ),
    ]
