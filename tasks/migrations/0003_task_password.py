# Generated by Django 3.2.15 on 2023-07-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20230709_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='password',
            field=models.CharField(default='company123', max_length=65, verbose_name='driver Password'),
        ),
    ]
