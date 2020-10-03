# Generated by Django 2.2.13 on 2020-10-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.CharField(blank=True, default='', max_length=11, verbose_name='手机号码'),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='真实姓名'),
        ),
    ]
