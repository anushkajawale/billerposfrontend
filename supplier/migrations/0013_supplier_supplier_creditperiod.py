# Generated by Django 5.1.6 on 2025-04-05 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0012_supplier_supplier_creditlimit'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='supplier_CreditPeriod',
            field=models.IntegerField(default=0),
        ),
    ]
