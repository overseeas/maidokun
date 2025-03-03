from django.db import models

# Create your models here.
class Margin(models.Model):
    group_name = models.CharField(unique=True, null=True)
    rate = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    def __str__(self):
        return self.group_name

class Item(models.Model):
    # 自社コード
    code = models.CharField(unique=True)
    # 商品名
    name = models.CharField(null=True)
    # 品番
    product_code = models.CharField(null=True)
    # JANコード
    jan_code = models.CharField(null=True)
    # 定価
    list_price = models.DecimalField(decimal_places=0, max_digits=10, null=True)
    # 実売価格
    sales_price = models.DecimalField(decimal_places=0, max_digits=10, null=True)
    # 在庫数
    stock_count = models.DecimalField(decimal_places=0, max_digits=10, null=True)
    # セール価格
    bargain_price = models.DecimalField(decimal_places=0, max_digits=10, null=True)
    # 発注型番
    model_number = models.CharField(null=True)
    # 原価
    cost = models.DecimalField(decimal_places=0, max_digits=10, null=True)
    # 送料グループ
    postage = models.CharField(null=True)
    # 発注グループ
    supplier = models.CharField(null=True)
    # 発注分類
    classification = models.CharField(null=True)
    # メーカー
    maker = models.CharField(null=True)
    # 掛率表カテゴリ
    category = models.CharField(null=True)
    # 廃番削除
    is_deleted = models.BooleanField(default=False)
    # 非表示
    is_visible = models.BooleanField(default=False)

    def __str__(self):
        return self.code
