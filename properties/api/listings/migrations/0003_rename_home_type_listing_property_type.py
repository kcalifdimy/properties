# Generated by Django 3.2.14 on 2022-08-18 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20220817_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='home_type',
            new_name='property_type',
        ),
    ]
