# Generated by Django 3.1.2 on 2020-11-23 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_pet_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='image_url',
            new_name='image_urll',
        ),
    ]
