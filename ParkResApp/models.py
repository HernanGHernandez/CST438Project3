from django.db import models
from django_filters import FilterSet
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.userId) + self.username


# class Parking(models.Model):
#     parkingId = models.AutoField(primary_key=True)
#     slot = models.IntegerField()
#     lot = models.CharField(max_length=50)
#     parkSwitch = models.BooleanField(default=True)
#     userId = models.ForeignKey(User, on_delete=models.CASCADE)
class LotA(models.Model):
    LotAId = models.AutoField(primary_key=True)
    space = models.IntegerField(default=0, validators=[
                                MaxValueValidator(50), MinValueValidator(1)])
    takenBool = models.BooleanField(default=False)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


class LotB(models.Model):
    LotBId = models.AutoField(primary_key=True)
    space = models.IntegerField(default=0, validators=[
                                MaxValueValidator(50), MinValueValidator(1)])
    takenBool = models.BooleanField(default=False)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


class LotC(models.Model):
    LotCId = models.AutoField(primary_key=True)
    space = models.IntegerField(default=0, validators=[
                                MaxValueValidator(50), MinValueValidator(1)])
    takenBool = models.BooleanField(default=False)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


class LotD(models.Model):
    LotDId = models.AutoField(primary_key=True)
    space = models.IntegerField(default=0, validators=[
                                MaxValueValidator(50), MinValueValidator(1)])
    takenBool = models.BooleanField(default=False)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


class Messages(models.Model):
    messageId = models.AutoField(primary_key=True)
    message = models.CharField(max_length=50)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    # LotAId = models.ForeignKey(LotA, on_delete=models.CASCADE)
    # LotBId = models.ForeignKey(LotB, on_delete=models.CASCADE)
    # LotCId = models.ForeignKey(LotC, on_delete=models.CASCADE)
    # LotDId = models.ForeignKey(LotD, on_delete=models.CASCADE)
