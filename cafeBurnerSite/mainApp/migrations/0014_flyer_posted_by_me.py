# Generated by Django 3.2.4 on 2022-03-28 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_flyer_posistion'),
    ]

    operations = [
        migrations.AddField(
            model_name='flyer',
            name='Posted_by_me',
            field=models.BooleanField(default=True),
        ),
    ]
