# Generated by Django 5.1.6 on 2025-03-28 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_barcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='taxtype',
        ),
        migrations.AlterField(
            model_name='product',
            name='taxpercent',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
