# Generated by Django 3.2.4 on 2022-07-06 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0026_auto_20220621_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='flyer',
            new_name='Flyer',
        ),
        migrations.RenameField(
            model_name='flyer_image',
            old_name='Url',
            new_name='Img_src_url',
        ),
    ]
