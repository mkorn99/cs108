# Generated by Django 2.2.7 on 2020-04-05 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0005_auto_20200401_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_file',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
