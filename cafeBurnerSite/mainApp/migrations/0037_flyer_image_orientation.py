# Generated by Django 3.2.4 on 2022-09-11 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0036_auto_20220809_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='flyer_image',
            name='Orientation',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
