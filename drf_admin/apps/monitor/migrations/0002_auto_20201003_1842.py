# Generated by Django 2.2.13 on 2020-10-03 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='errorlogs',
            old_name='name',
            new_name='username',
        ),
    ]
