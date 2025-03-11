from django.db import models

# Create your models here.
class Postage(models.Model):
    name = models.CharField(unique=True)
    def __str__(self):
        return self.name
class Supplier(models.Model):
    name = models.CharField(unique=True)
    def __str__(self):
        return self.name
class Classification(models.Model):
    name = models.CharField(unique=True)
    def __str__(self):
        return self.name
class Maker(models.Model):
    name = models.CharField(unique=True)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(unique=True)
    def __str__(self):
        return self.name

class Item(models.Model):
    # 自社コード
    code = models.CharField(unique=True)
    # 商品名
    name = models.CharField()
    # 品番
    # product_code = models.CharField(blank=True)
    # JANコード
    # jan_code = models.CharField(blank=True)
    # 定価
    list_price = models.IntegerField(blank=True)
    # 実売価格
    sales_price = models.IntegerField()
    # 在庫数
    # stock_count = models.IntegerField(blank=True)
    # セール価格
    # bargain_price = models.IntegerField(blank=True)
    # 発注型番
    model_number = models.CharField()
    # 原価
    cost = models.CharField()
    # 送料グループ
    postage = models.ForeignKey(Postage, on_delete=models.CASCADE)
    # 発注グループ
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    # 発注分類
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    # メーカー
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    # 掛率表カテゴリ
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 廃番削除
    is_deleted = models.BooleanField(default=False)
    # 非表示
    is_visible = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
