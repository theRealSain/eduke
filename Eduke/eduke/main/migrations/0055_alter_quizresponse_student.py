# Generated by Django 5.1.6 on 2025-04-08 10:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0054_alter_quizzes_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizresponse',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.students'),
        ),
    ]
