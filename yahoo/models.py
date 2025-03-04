from django.db import models

# Create your models here.
class Item(models.Model):
    # パス
    path = models.CharField()
    # 商品名
    name = models.CharField()
    # 商品コード
    code = models.CharField()
    # 個別商品コード
    sub_code = models.CharField(blank=True)
    # メーカー希望小売価格
    original_price = models.DecimalField(decimal_places=0, max_digits=10, blank=True)
    # 通常販売価格
    price = models.DecimalField(decimal_places=0, max_digits=10)
    # 特価
    sale_price = models.DecimalField(decimal_places=0, max_digits=10, blank=True)
    # オプション
    options = models.TextField(blank=True)
    # 重量
    ship_weight = models.DecimalField(decimal_places=0, max_digits=10, blank=True)
    # ページ公開
    display = models.BooleanField(default=False)
    # 送料無料
    delivery = models.CharField(blank=True)
    # プロダクトカテゴリ
    product_category = models.CharField()
    # スペック
    spec1 = models.CharField(blank=True)
    # スペック
    spec2 = models.CharField(blank=True)
    # スペック
    spec3 = models.CharField(blank=True)
    # スペック
    spec4 = models.CharField(blank=True)
    # スペック
    spec5 = models.CharField(blank=True)
    
    # 廃番?
    is_deleted = models.BooleanField(default=False)

    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.code
