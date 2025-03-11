from django.db import models
import item.models

# Create your models here.
class YahooMaidoItem(models.Model):
    # パス
    path = models.CharField()
    # 商品名
    name = models.CharField()
    # 商品コード
    # code = models.CharField(null=True)
    # 個別商品コード
    # sub_code = models.CharField(blank=True)
    # メーカー希望小売価格
    # original_price = models.IntegerField(blank=True)
    # 通常販売価格
    price = models.IntegerField()
    # 特価
    # sale_price = models.IntegerField(blank=True)
    # オプション
    # options = models.TextField(blank=True)
    # 重量
    # ship_weight = models.IntegerField(blank=True)
    # ページ公開
    # display = models.BooleanField(default=False)
    # 送料無料
    # delivery = models.CharField(blank=True)
    # プロダクトカテゴリ
    product_category = models.CharField()
    # スペック
    # spec1 = models.CharField(blank=True)
    # スペック
    # spec2 = models.CharField(blank=True)
    # スペック
    # spec3 = models.CharField(blank=True)
    # スペック
    # spec4 = models.CharField(blank=True)
    # スペック
    # spec5 = models.CharField(blank=True)
    
    # 廃番?
    is_deleted = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #関係
    item = models.ForeignKey(item.models.Item, on_delete=models.CASCADE)
    def __str__(self):
        return self.item.code

class YahooCoordiroomItem(models.Model):
    # パス
    path = models.CharField()
    # 商品名
    name = models.CharField()
    # 商品コード
    # code = models.CharField(null=True)
    # 個別商品コード
    # sub_code = models.CharField(blank=True)
    # メーカー希望小売価格
    # original_price = models.IntegerField(blank=True)
    # 通常販売価格
    price = models.IntegerField()
    # 特価
    # sale_price = models.IntegerField(blank=True)
    # オプション
    # options = models.TextField(blank=True)
    # 重量
    # ship_weight = models.IntegerField(blank=True)
    # ページ公開
    # display = models.BooleanField(default=False)
    # 送料無料
    # delivery = models.CharField(blank=True)
    # プロダクトカテゴリ
    product_category = models.CharField(blank=True)
    # スペック
    # spec1 = models.CharField(blank=True)
    # スペック
    # spec2 = models.CharField(blank=True)
    # スペック
    # spec3 = models.CharField(blank=True)
    # スペック
    # spec4 = models.CharField(blank=True)
    # スペック
    # spec5 = models.CharField(blank=True)
    
    # 廃番?
    is_deleted = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #関係
    item = models.ForeignKey(item.models.Item, on_delete=models.CASCADE)
    def __str__(self):
        return self.item.code
