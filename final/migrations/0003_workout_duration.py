# Generated by Django 2.2.7 on 2020-04-16 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0002_remove_profile_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='duration',
            field=models.TextField(blank=True),
        ),
    ]
