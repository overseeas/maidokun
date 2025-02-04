from django.db import models

# Create your models here.
class Margin(models.Model):
    group_name = models.CharField(unique=True, null=True)
    rate = models.DecimalField(decimal_places=2, max_digits=5, null=True)

class Item(models.Model):
    item_code = models.CharField(unique=True)

    #maker info
    maker_price = models.DecimalField(decimal_places=0, max_digits=10, null=True)
    maker_code = models.CharField(null=True)
     
    #relationships
    margin_rate = models.ForeignKey(Margin, on_delete=models.CASCADE, null=True)

