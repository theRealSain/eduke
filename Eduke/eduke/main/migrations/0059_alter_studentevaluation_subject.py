# Generated by Django 5.1.6 on 2025-04-08 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0058_alter_quizquestions_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentevaluation',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.subjects'),
        ),
    ]
