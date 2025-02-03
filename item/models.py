from django.db import models

# Create your models here.
class Margin(models.Model):
    pass

class Item(models.Model):
    item_code = models.CharField(unique=True)

    #maker info
    maker_price = models.DecimalField(decimal_places)
    maker_code = models.CharField()
     
    #relationships
    margin_rate = models.ForeignKey(Margin, on_delete=models.CASCADE)

