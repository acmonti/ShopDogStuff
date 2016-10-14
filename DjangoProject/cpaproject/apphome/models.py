from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Clothes (models.Model):
    image = models.FileField(null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    stocks = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Clothes'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
