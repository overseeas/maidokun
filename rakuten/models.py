import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Item(models.Model):
    manage_number = models.CharField(max_length=255)
    title = models.TextField()
    hide_item = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.manage_number


class Sku(models.Model):
    sku_number = models.CharField(max_length=255)
    standard_price = models.IntegerField(default=0)
    reference_price = models.CharField(max_length=255)
    hidden = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return self.sku_number