# Generated by Django 3.2.4 on 2022-08-02 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0033_alter_flyer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flyer',
            name='Description',
            field=models.CharField(default='Come by !', max_length=500, null=True),
        ),
    ]
