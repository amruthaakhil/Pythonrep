# Generated by Django 4.2.9 on 2024-01-20 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_rename_tasks_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1222-02-22'),
            preserve_default=False,
        ),
    ]
