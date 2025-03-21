# Generated by Django 5.1.4 on 2025-02-09 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_quizresponse_question_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizQuestions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('option_a', models.CharField(max_length=255)),
                ('option_b', models.CharField(max_length=255)),
                ('option_c', models.CharField(max_length=255)),
                ('option_d', models.CharField(max_length=255)),
                ('correct_option', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='QuizResponse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_response', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.quizquestions')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.students')),
            ],
        ),
        migrations.CreateModel(
            name='Quizzes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('class_obj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.classes')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subjects')),
            ],
        ),
        migrations.AddField(
            model_name='quizquestions',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.quizzes'),
        ),
    ]
