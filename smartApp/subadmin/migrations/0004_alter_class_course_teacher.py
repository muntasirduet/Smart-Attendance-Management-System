# Generated by Django 3.2.18 on 2023-03-04 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subadmin', '0003_alter_class_course_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='course_teacher',
            field=models.CharField(max_length=50),
        ),
    ]