from django.contrib.auth.models import User
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}"


class Offer(models.Model):
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    max_number_of_travelers = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"Offer for {self.city.name}"


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    offer = models.ForeignKey(Offer, on_delete=models.DO_NOTHING)
    number_of_travelers = models.IntegerField()
    final_price = models.FloatField()
    is_finalized = models.BooleanField()

    def __str__(self):
        return f"basket of user: {self.user.username}"
