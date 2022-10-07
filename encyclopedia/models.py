from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=20, unique=True)


class Fish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    scientific = models.CharField(max_length=200, unique=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
