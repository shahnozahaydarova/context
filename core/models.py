from django.db import models

class car(models.Model):
    brand = models.CharField(max_length=14)
    color = models.CharField(max_length=12)
    img = models.CharField(max_length=255)
    def __str__(self):
        return self.brand


class telephone(models.Model):
    brand = models.CharField(max_length=14)
    color = models.CharField(max_length=12)
    img = models.CharField(max_length=255)
    def __str__(self):
        return self.brand

class flower(models.Model):
    type = models.CharField(max_length=14)
    color = models.CharField(max_length=12)
    img = models.CharField(max_length=255)
    def __str__(self):
        return self.type

class komputer(models.Model):
    brand = models.CharField(max_length=14)
    color = models.CharField(max_length=12)
    img = models.CharField(max_length=255)
    def __str__(self):
        return self.brand

class TVset(models.Model):
    brand = models.CharField(max_length=14)
    color = models.CharField(max_length=12)
    img = models.CharField(max_length=255)
    def __str__(self):
        return self.brand