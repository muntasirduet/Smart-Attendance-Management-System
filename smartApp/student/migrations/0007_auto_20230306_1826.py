# Generated by Django 3.2.18 on 2023-03-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_studentlist_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentlist',
            name='section',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='studentlist',
            name='semister',
            field=models.CharField(default='', max_length=50),
        ),
    ]