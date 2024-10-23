# Generated by Django 5.1.1 on 2024-10-22 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('avg_temp', models.FloatField()),
                ('max_temp', models.FloatField()),
                ('min_temp', models.FloatField()),
                ('dominant_weather', models.CharField(max_length=50)),
            ],
        ),
    ]
