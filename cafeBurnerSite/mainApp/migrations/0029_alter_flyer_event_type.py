# Generated by Django 3.2.4 on 2022-07-24 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0028_alter_flyer_contact_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flyer',
            name='Event_type',
            field=models.CharField(choices=[('comedy', 'Comedy'), ('food', 'Food'), ('athletic', 'Athletic'), ('outdoor', 'Outdoor'), ('sports', 'Sports'), ('seasonal', 'Seasonal'), ('rock', 'Live Music: Rock'), ('drinks', 'Drinks'), ('hipHop', 'Live Music: HipHop'), ('dance', 'Live Music: Dance'), ('other', 'Live Music: Other'), ('community', 'Community'), ('class', 'Class / Info')], max_length=10),
        ),
    ]
