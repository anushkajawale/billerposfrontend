# Generated by Django 5.1.6 on 2025-03-30 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_alter_users_users_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='users_name',
            field=models.CharField(default='Cash', max_length=255),
        ),
        migrations.AddField(
            model_name='users',
            name='users_pass',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
