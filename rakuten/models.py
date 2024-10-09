from django.db import models
from django.utils import timezone

import datetime


# Create your models here.

class Item(models.Model):
    #商品管理番号
    manageNumber = models.CharField(max_length=255, null=True)
    #商品番号
    itemNumber = models.CharField(max_length=255, null=True)
    #商品名
    title = models.CharField(null=True)
    #キャッチコピー
    tagline = models.CharField(null=True)
    #PC用商品説明文
    productDescription_pc = models.TextField(null=True)
    #スマートフォン用商品説明文
    productDescription_sp = models.TextField(null=True)
    #PC用販売説明文
    salesDescription = models.TextField(null=True)
    #商品種別
    itemType = models.CharField(null=True)
    #ジャンルID
    genreId = models.CharField(null=True)
    #非製品属性タグID
    tags = models.CharField(null=True)
    #倉庫指定
    hideItem = models.BooleanField(null=True)
    #サーチ表示
    features_searchVisibility = models.CharField(null=True)
    #注文ボタン表示
    features_displayNormalCartButton = models.BooleanField(null=True)
    #在庫表表示
    features_inventoryDisplay = models.CharField(null=True)
    #お問い合わせボタン表示
    features_shopContact = models.BooleanField(null=True)
    #消費税込み
    payment_taxIncluded = models.BooleanField(null=True)
    #代引料
    payment_cashOnDeliveryFeeIncluded = models.BooleanField(null=True)

    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.manageNumber


class Sku(models.Model):
    #sku管理番号
    skuNumber = models.CharField(max_length=255, null=True)
    #表示価格種別
    referencePrice_displayType = models.CharField(max_length=255, null=True)
    #表示価格
    referencePrice_value = models.CharField(null=True)
    #SKU倉庫設定
    hidden = models.BooleanField(null=True)
    #販売価格
    standardPrice = models.IntegerField(null=True)

    #カタログID
    articleNumber_value = models.CharField(null=True)
    #カタログIDなしの理由
    articleNumber_exemptionReason = models.CharField(null=True)

    updated_at = models.DateTimeField(auto_now=True)

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return self.skuNumber