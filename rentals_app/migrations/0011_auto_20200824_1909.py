# Generated by Django 3.1 on 2020-08-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals_app', '0010_reservation_occasion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='approved',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='picked_up',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]