# Generated by Django 5.1.6 on 2025-03-21 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0009_supplier_supplier_billingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='supplier_ShippingAddress',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
