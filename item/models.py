from django.db import models

# Create your models here.
class Item(models.Model):
    item_code = models.CharField(unique=True)
