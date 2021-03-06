# Generated by Django 3.1 on 2020-08-23 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='display_name',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
