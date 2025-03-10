from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField()
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField()
    def __str__(self):
        return self.name

class Item(models.Model):
    # 商品番号
    number = models.DecimalField(decimal_places=0, max_digits=10)
    # 商品名
    name = models.CharField()
    # 型番/品番
    code = models.CharField()
    # カテゴリ
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # サブカテゴリ
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True)
    # 販売価格
    price = models.DecimalField(decimal_places=0, max_digits=10)
    # 希望小売価格
    retail_price = models.CharField(blank=True)
    # 在庫数
    stock = models.DecimalField(decimal_places=0, max_digits=10)
    # 準備中（True:0、False:1）
    is_visible = models.BooleanField(default=False)
    # 管理用メモ
    comment = models.CharField(blank=True)

    # 廃番?
    is_deleted = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.c
