from django.db import models

# Create your models here.


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Parking(models.Model):
    parkingId = models.AutoField(primary_key=True)
    slot = models.IntegerField()
    lot = models.CharField(max_length=50)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


class Messages(models.Model):
    messageId = models.AutoField(primary_key=True)
    message = models.CharField(max_length=50)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    parkingId = models.ForeignKey(Parking, on_delete=models.CASCADE)
