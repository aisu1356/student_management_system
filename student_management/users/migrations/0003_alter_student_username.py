# Generated by Django 5.1.7 on 2025-03-21 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_student_options_alter_student_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
