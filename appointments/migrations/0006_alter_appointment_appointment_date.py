# Generated by Django 5.1.5 on 2025-02-05 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_remove_appointment_duration_minutes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(),
        ),
    ]
