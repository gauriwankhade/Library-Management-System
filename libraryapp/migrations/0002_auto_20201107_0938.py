# Generated by Django 3.1.3 on 2020-11-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='member_type',
        ),
        migrations.AddField(
            model_name='member',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
    ]
