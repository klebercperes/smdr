from django.db import models

class SMDRData(models.Model):
    station_number = models.IntegerField()
    co = models.IntegerField()
    time = models.TimeField()
    start = models.DateTimeField()
    direction = models.CharField(max_length=10)
    cli = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    account_code = models.CharField(max_length=50)

    def __str__(self):
        return f"Station: {self.station_number}, Time: {self.time}, Start: {self.start}"
