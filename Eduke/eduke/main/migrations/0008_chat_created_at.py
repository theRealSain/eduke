# Generated by Django 5.1.4 on 2025-01-27 17:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_student_attendance_student_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
