# Generated by Django 5.1.6 on 2025-03-21 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('tax_id', models.AutoField(primary_key=True, serialize=False)),
                ('tax_name', models.CharField(max_length=255)),
                ('tax_percentage', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'tbl_tax',
            },
        ),
    ]
