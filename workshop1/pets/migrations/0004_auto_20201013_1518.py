# Generated by Django 3.1.2 on 2020-10-13 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_pet_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image_url',
            field=models.URLField(),
        ),
    ]
