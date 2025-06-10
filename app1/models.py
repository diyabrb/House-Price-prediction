from django.db import models

# Create your models here.
class Housedata(models.Model):
    MedInc=models.FloatField()
    HouseAge=models.FloatField()
    AveRooms=models.FloatField()
    AveBedrms=models.FloatField()
    Population=models.FloatField()
    AveOccup=models.FloatField()
    Latitude=models.FloatField()
    Longitude=models.FloatField()
    target=models.IntegerField()


