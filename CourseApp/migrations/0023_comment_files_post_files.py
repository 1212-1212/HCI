# Generated by Django 4.1 on 2022-09-22 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseApp', '0022_remove_post_topic_comment_content_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='files',
            field=models.FileField(blank=True, default='', upload_to='student_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='files',
            field=models.FileField(blank=True, default='', upload_to='student_images/'),
        ),
    ]
