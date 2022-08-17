# Generated by Django 3.2.14 on 2022-08-17 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='photo_1',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_10',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_11',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_12',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_13',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_14',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_15',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_16',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_17',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_18',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_19',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_2',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_20',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_3',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_4',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_5',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_6',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_7',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_8',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_9',
        ),
        migrations.AlterField(
            model_name='listing',
            name='lister',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to=settings.AUTH_USER_MODEL),
        ),
    ]
