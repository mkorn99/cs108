# Generated by Django 2.2.7 on 2020-04-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0004_remove_workout_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]