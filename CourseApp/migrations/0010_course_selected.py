# Generated by Django 4.1 on 2022-09-10 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseApp', '0009_alter_instructor_email_alter_learner_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]