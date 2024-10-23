from django.db import models

class WeatherSummary(models.Model):
    date = models.DateField()
    average_temperature = models.FloatField()
    max_temperature = models.FloatField()
    min_temperature = models.FloatField()
    dominant_condition = models.CharField(max_length=100)

    def __str__(self):
        return f"Weather Summary for {self.date}"
