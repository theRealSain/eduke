# Generated by Django 5.1.4 on 2025-02-09 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_quizresponse_quiz_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizresponse',
            name='student_response',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=2, null=True),
        ),
    ]
