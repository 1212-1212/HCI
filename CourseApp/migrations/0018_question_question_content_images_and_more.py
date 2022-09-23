# Generated by Django 4.1 on 2022-09-21 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseApp', '0017_remove_lesson_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_content_images',
            field=models.FileField(blank=True, null=True, upload_to='question_images/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_content',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]