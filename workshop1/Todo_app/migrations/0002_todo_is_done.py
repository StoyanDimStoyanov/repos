# Generated by Django 3.1.2 on 2020-10-08 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]