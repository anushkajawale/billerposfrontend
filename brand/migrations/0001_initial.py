# Generated by Django 5.1.6 on 2025-03-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=255)),
                ('brand_img', models.ImageField(upload_to='brand/')),
            ],
            options={
                'db_table': 'tbl_brand',
            },
        ),
    ]
