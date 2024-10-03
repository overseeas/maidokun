from django.db import models
from django.utils import timezone

import datetime


# Create your models here.

class Item(models.Model):
    #商品管理番号
    manageNumber = models.CharField(max_length=255)
    #商品番号
    itemNumber = models.CharField(max_length=255)
    #商品名
    title = models.TextField(blank=True)
    #キャッチコピー
    tagline = models.TextField(blank=True)
    #PC用商品説明文
    productDescription_pc = models.TextField(blank=True)
    #スマートフォン用商品説明文
    productDescription_sp = models.TextField(blank=True)
    #PC用販売説明文
    salesDescription = models.TextField(blank=True)
    #医薬品説明文
    precautions_description = models.TextField(blank=True)
    #医薬品注意事項	
    precautions_agreement = models.TextField(blank=True)
    #商品種別
    itemType = models.CharField(blank=True)
    #商品画像種別
    images_type = models.CharField(blank=True)
    #商品画像URL
    images_location = models.URLField(blank=True)
    #商品画像名（ALT）
    images_alt = models.CharField(blank=True)
    #白背景画像種別	
    whiteBgImage_type = models.CharField(blank=True)
    #白背景画像URL
    whiteBgImage_location = models.URLField(blank=True)
    #動画種別
    video_type = models.CharField(blank=True)
    #動画のURL
    video_parameters_value = models.URLField(blank=True)
    #ジャンルID
    genreId = models.CharField()
    #非製品属性タグID
    tags = models.TextField()
    #倉庫指定
    hideItem = models.BooleanField()


    #消費税込み
    payment_taxIncluded = models.BooleanField()
    #サーチ表示
    features_searchVisibility = models.CharField()
    #注文ボタン表示
    features_displayNormalCartButton = models.BooleanField()
    #在庫表表示
    features_inventoryDisplay = models.CharField()
    #お問い合わせボタン表示
    features_shopContact = models.BooleanField()
    #代引料
    payment_cashOnDeliveryFeeIncluded = models.BooleanField()






    updated_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.manage_number


class Sku(models.Model):
    #sku管理番号
    skuNumber = models.CharField(max_length=255)
    #販売価格
    standardPrice = models.IntegerField()
    #表示価格種別
    referencePrice_displayType = models.CharField(max_length=255)
    #表示価格
    referencePrice_value = models.CharField()
    #SKU倉庫設定
    hidden = models.IntegerField(default=0)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return self.sku_number