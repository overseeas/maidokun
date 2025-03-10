from django.db import models
import item.models

# Create your models here.
class Stock(models.Model):
    name = models.CharField()
    def __str__(self):
        return self.name

class Deliverygroup(models.Model):
    name = models.CharField()
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField()
    def __str__(self):
        return self.name

class Maker(models.Model):
    name = models.CharField()
    def __str__(self):
        return self.name

class KakakuStore1Item(models.Model):
    # JAN
    jan = models.CharField(blank=True)
    # 価格.comの製品名・型番
    code = models.CharField()
    # 登録価格
    price = models.IntegerField(blank=True)
    # 送料
    delivery = models.IntegerField()
    # 在庫・発送
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, blank=True)
    # 送料区分
    delivery_group = models.ForeignKey(Deliverygroup, on_delete=models.CASCADE, blank=True)
    # 店頭
    store = models.BooleanField(default=False)
    # カテゴリ
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    # メーカー
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE, blank=True)
    # リンク先URL
    link = models.URLField(blank=True)
    # 画像URL
    image_url = models.URLField(blank=True)
    # 一言コメント
    comment = models.CharField(blank=True)
    # 延長保証
    warranty = models.BooleanField(blank=True)




    # 廃番?
    is_deleted = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #関係
    item = models.ForeignKey(item.models.Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.c

class KakakuStore2Item(models.Model):
    # JAN
    jan = models.CharField(blank=True)
    # 価格.comの製品名・型番
    code = models.CharField()
    # 登録価格
    price = models.IntegerField(blank=True)
    # 送料
    delivery = models.IntegerField()
    # 在庫・発送
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, blank=True)
    # 送料区分
    delivery_group = models.ForeignKey(Deliverygroup, on_delete=models.CASCADE, blank=True)
    # 店頭
    store = models.BooleanField(default=False)
    # カテゴリ
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    # メーカー
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE, blank=True)
    # リンク先URL
    link = models.URLField(blank=True)
    # 画像URL
    image_url = models.URLField(blank=True)
    # 一言コメント
    comment = models.CharField(blank=True)
    # 延長保証
    warranty = models.BooleanField(blank=True)




    # 廃番?
    is_deleted = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #関係
    item = models.ForeignKey(item.models.Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.c
