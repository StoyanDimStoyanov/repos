# Generated by Django 3.1.2 on 2020-10-15 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
