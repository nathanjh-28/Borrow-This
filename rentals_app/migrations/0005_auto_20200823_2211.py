# Generated by Django 3.1 on 2020-08-23 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals_app', '0004_auto_20200823_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental_item',
            name='picture',
            field=models.URLField(blank=True),
        ),
    ]