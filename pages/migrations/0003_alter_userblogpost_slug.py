# Generated by Django 4.0.5 on 2022-06-26 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_userblogpost_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblogpost',
            name='slug',
            field=models.SlugField(unique_for_date='published'),
        ),
    ]
