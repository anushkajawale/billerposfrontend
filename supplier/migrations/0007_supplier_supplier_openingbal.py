# Generated by Django 5.1.6 on 2025-03-21 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0006_supplier_supplier_panno'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='supplier_openingbal',
            field=models.IntegerField(null=True),
        ),
    ]
