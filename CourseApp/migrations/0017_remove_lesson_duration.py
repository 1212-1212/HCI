# Generated by Django 4.1 on 2022-09-20 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CourseApp', '0016_lesson_link_alter_lesson_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='duration',
        ),
    ]
