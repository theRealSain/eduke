# Generated by Django 5.1.6 on 2025-04-08 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0057_alter_quizquestions_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestions',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.quizzes'),
        ),
    ]
