from django.db import models


class Staff(models.Model):
    account = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    title = models.CharField(max_length=50)
    details = models.TextField()

class Region(models.Model):
    name = models.CharField(max_length=20, unique=True)

class Fish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    scientific = models.CharField(max_length=200, unique=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
