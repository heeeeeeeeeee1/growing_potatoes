# Generated by Django 4.2.16 on 2024-09-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, upload_to='Move'),
        ),
    ]
