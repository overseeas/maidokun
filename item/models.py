from django.db import models

# Create your models here.
class Margin(models.Model):
    group_name = models.CharField(unique=True)
    rate = models.DecimalField(decimal_places=2, max_digits=5)
    def __str__(self):
        return self.group_name

class Item(models.Model):
    # 自社コード
    code = models.CharField(unique=True)
    # 商品名
    name = models.CharField()
    # 品番
    product_code = models.CharField(blank=True)
    # JANコード
    jan_code = models.CharField(blank=True)
    # 定価
    list_price = models.DecimalField(decimal_places=0, max_digits=10, blank=True)
    # 実売価格
    sales_price = models.DecimalField(decimal_places=0, max_digits=10)
    # 在庫数
    stock_count = models.DecimalField(decimal_places=0, max_digits=10, blank=True)
    # セール価格
    bargain_price = models.DecimalField(decimal_places=0, max_digits=10, blank=True)
    # 発注型番
    model_number = models.CharField()
    # 原価
    cost = models.DecimalField(decimal_places=0, max_digits=10)
    # 送料グループ
    postage = models.CharField()
    # 発注グループ
    supplier = models.CharField()
    # 発注分類
    classification = models.CharField()
    # メーカー
    maker = models.CharField()
    # 掛率表カテゴリ
    category = models.CharField()
    # 廃番削除
    is_deleted = models.BooleanField(default=False)
    # 非表示
    is_visible = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
