# Generated by Django 3.2.18 on 2023-03-07 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20230306_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentlist',
            name='department',
            field=models.CharField(default='', max_length=50),
        ),
    ]