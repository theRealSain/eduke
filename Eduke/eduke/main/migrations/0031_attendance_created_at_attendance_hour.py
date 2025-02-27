# Generated by Django 5.1.4 on 2025-02-22 06:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_studentevaluation_assignment_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='hour',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
