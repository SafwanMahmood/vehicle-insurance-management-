# Generated by Django 4.1.4 on 2022-12-21 00:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('risk_app', '0004_remove_customer_response_alter_customer_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='BirthDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
