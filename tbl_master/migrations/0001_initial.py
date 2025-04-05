# Generated by Django 5.1.6 on 2025-04-04 05:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0003_customer_customer_creditlimit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('master_id', models.AutoField(primary_key=True, serialize=False)),
                ('master_itemname', models.CharField(max_length=255)),
                ('master_qty', models.CharField(max_length=255)),
                ('master_mrp', models.CharField(max_length=255)),
                ('master_sale_price', models.CharField(max_length=255)),
                ('master_total', models.IntegerField()),
                ('master_payment_mode', models.CharField(max_length=255)),
                ('master_remaingamt', models.IntegerField()),
                ('master_billdate', models.DateTimeField()),
                ('master_totalAmount', models.IntegerField()),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
            options={
                'db_table': 'tbl_master',
            },
        ),
    ]
