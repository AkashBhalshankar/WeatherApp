# Generated by Django 3.2.25 on 2024-10-22 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('average_temperature', models.FloatField()),
                ('max_temperature', models.FloatField()),
                ('min_temperature', models.FloatField()),
                ('dominant_condition', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='WeatherData',
        ),
    ]
