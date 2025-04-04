# Generated by Django 5.1.4 on 2025-01-22 03:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_institution_institution_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='student',
            new_name='student_id',
        ),
        migrations.RenameField(
            model_name='attendance',
            old_name='subject',
            new_name='subject_id',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='receiver',
            new_name='receiver_id',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='sender',
            new_name='sender_id',
        ),
        migrations.RenameField(
            model_name='classes',
            old_name='institution',
            new_name='institution_id',
        ),
        migrations.RenameField(
            model_name='institution',
            old_name='id',
            new_name='institution_id',
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='student',
            new_name='student_id',
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='subject',
            new_name='subject_id',
        ),
        migrations.RenameField(
            model_name='quizzes',
            old_name='subject',
            new_name='subject_id',
        ),
        migrations.RenameField(
            model_name='studentevaluations',
            old_name='student',
            new_name='student_id',
        ),
        migrations.RenameField(
            model_name='subjects',
            old_name='class_obj',
            new_name='class_id',
        ),
        migrations.RenameField(
            model_name='teachers',
            old_name='institution',
            new_name='institution_id',
        ),
        migrations.RemoveField(
            model_name='quizzes',
            name='class_obj',
        ),
        migrations.RemoveField(
            model_name='students',
            name='class_obj',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='class_obj',
        ),
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
        migrations.RemoveField(
            model_name='users',
            name='name',
        ),
        migrations.AddField(
            model_name='parents',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='quizzes',
            name='class_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.classes'),
        ),
        migrations.AddField(
            model_name='quizzes',
            name='correct_option',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='quizzes',
            name='option_a',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='quizzes',
            name='option_b',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='quizzes',
            name='option_c',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='quizzes',
            name='option_d',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='quizzes',
            name='question',
            field=models.TextField(default='Default Question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='student_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.students'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='student_response',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='students',
            name='class_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.classes'),
        ),
        migrations.AddField(
            model_name='students',
            name='name',
            field=models.CharField(default='Default Name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers',
            name='class_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.classes'),
        ),
        migrations.AddField(
            model_name='teachers',
            name='name',
            field=models.CharField(default='Defualt Name', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='institution',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='parents',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='parents',
            name='student_roll_no',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.students', to_field='roll_no'),
        ),
        migrations.AlterField(
            model_name='parents',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.users'),
        ),
        migrations.AlterField(
            model_name='studentevaluations',
            name='class_difficulty_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentevaluations',
            name='class_participation_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentevaluations',
            name='focus_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentevaluations',
            name='homework_completion_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentevaluations',
            name='parent_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentevaluations',
            name='sleep_time_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentevaluations',
            name='stress_handling_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentevaluations',
            name='study_time_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentevaluations',
            name='teacher_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentevaluations',
            name='test_preparation_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='students',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='students',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.users'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.users'),
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student'), ('parent', 'Parent')], max_length=20),
        ),
        migrations.DeleteModel(
            name='QuestionsResponses',
        ),
    ]
