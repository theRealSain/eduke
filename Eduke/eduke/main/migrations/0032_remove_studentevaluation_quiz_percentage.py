# Generated by Django 5.1.4 on 2025-02-23 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_attendance_created_at_attendance_hour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentevaluation',
            name='quiz_percentage',
        ),
    ]
