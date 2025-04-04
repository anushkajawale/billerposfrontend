# Generated by Django 5.1.6 on 2025-04-04 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0003_customer_customer_creditlimit_and_more'),
        ('product', '0006_alter_product_purchase'),
        ('tbl_master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poschild',
            fields=[
                ('posch_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('master_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tbl_master.master')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'tbl_poschild',
            },
        ),
    ]
