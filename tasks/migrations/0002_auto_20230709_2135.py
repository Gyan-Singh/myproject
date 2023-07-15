# Generated by Django 3.2.15 on 2023-07-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.AddField(
            model_name='task',
            name='email',
            field=models.CharField(default=None, max_length=65, unique=True, verbose_name='driver email'),
        ),
        migrations.AddField(
            model_name='task',
            name='id_num',
            field=models.IntegerField(default=None, unique=True, verbose_name='driver id number'),
        ),
        migrations.AddField(
            model_name='task',
            name='phone',
            field=models.IntegerField(default=None, unique=True, verbose_name='driver number'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=65, verbose_name='driver name'),
        ),
    ]
