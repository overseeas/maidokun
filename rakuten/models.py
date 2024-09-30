from django.db import models
from django.utils import timezone

import datetime


# Create your models here.

class Item(models.Model):
    #商品管理番号（商品URL）
    manage_number = models.CharField(max_length=255)
    #商品番号
    item_number = models.CharField(max_length=255)
    #商品名
    title = models.TextField()
    #倉庫指定
    hide_item = models.BooleanField()
    #サーチ表示
    tagline = models.BooleanField()
    #消費税
    tax = models.BooleanField()
    #注文ボタン表示
    order_button = models.BooleanField()
    #お問い合わせボタン表示
    shop_contact_button = models.BooleanField()
    #在庫表表示
    inventory_display = models.IntegerField()

    updated_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.manage_number


class Sku(models.Model):
    sku_number = models.CharField(max_length=255)
    standard_price = models.IntegerField(default=0)
    reference_price = models.CharField(max_length=255)
    hidden = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return self.sku_number