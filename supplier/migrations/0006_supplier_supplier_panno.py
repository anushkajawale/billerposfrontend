# Generated by Django 5.1.6 on 2025-03-21 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0005_supplier_supplier_gstno'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='supplier_panno',
            field=models.IntegerField(null=True),
        ),
    ]
