# Generated by Django 3.2.6 on 2021-08-23 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodsewabackend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='password',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='re_enter',
        ),
        migrations.AlterField(
            model_name='signup',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
