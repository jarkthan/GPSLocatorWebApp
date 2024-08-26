# Generated by Django 5.1 on 2024-08-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holes',
            fields=[
                ('HoleId', models.IntegerField(primary_key=True, serialize=False)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Description', models.TextField(blank=True)),
                ('Image', models.ImageField(blank=True, upload_to='hole_image/')),
                ('Modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
