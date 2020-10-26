# Generated by Django 3.1.2 on 2020-10-13 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_auto_20201013_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='description',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
