from django.db import models
from django.utils import timezone
from item.models import Item as ItemItem

import datetime


# Create your models here.
class Item(models.Model):
    #商品管理番号
    manageNumber = models.CharField()
    #商品番号
    #itemNumber = models.CharField(max_length=255, blank=True)
    #商品名
    title = models.CharField()
    #キャッチコピー
    #tagline = models.CharField(blank=True)
    #商品説明文
    #productDescription = models.JSONField(default=dict(pc="PC要商品説明文", sp="スマートフォン要商品説明文"))
    #PC用販売説明文
    #salesDescription = models.TextField(blank=True)
    #医薬品説明文・注意事項
    #precautions = models.JSONField(default = dict(description= "医薬品説明文", agreement= "医療品注意事項"))
    #商品種別
    # itemType = models.CharField(choices=[("NORMAL", "通常商品"), ("PRE_ORDER", "予約商品"), ("SUBSCRIPTION", "定期購入商品")])
    #商品画像
    #images = models.JSONField(default=dict(images=[dict(type="商品画像種別",location="商品画像種別",alt="商品画像名（ALT）")]))
    #白背景画像
    #whiteBgImage = models.JSONField(default=dict(type= "白背景画像種別", location= "白背景画像URL"))
    #動画
    #video = models.JSONField(default=dict(type= "動画種別", parameters= dict(value= "動画のURL")))
    #ジャンルID
    # genreId = models.CharField()
    #非製品属性タグID
    #tags = models.JSONField(default=dict(tags= []))
    #倉庫指定
    # hideItem = models.BooleanField(default=True)
    #在庫設定なし
    # unlimitedInventoryFlag = models.BooleanField()
    #商品オプション（項目選択肢）
    #customizationOptions = models.JSONField(default=dict(customizationOptions= [dict(displayName= "商品オプション（項目選択肢）項目名", inputType= "商品オプション選択肢タイプ", required= "商品オプション必須フラグ", selections= [dict(displayValue= "商品オプション選択肢名")])]))
    #予約商品発売日
    #releaseDate = models.DateField(blank=True)
    #販売期間指定
    #purchasablePeriod = models.JSONField(default=dict(start="販売開始日時", end="販売終了日時"))
    #定期購入商品設定
    #subscription = models.JSONField(default=dict(shippingDateFlag= "お届け日付指定フラグ", shippingIntervalFlag= "お届け間隔指定フラグ"))
    #その他設定
    # features = models.JSONField(default=dict(searchVisiblity= "サーチ表示", displayNormalCartButton= "注文ボタン", displaySubscriptionCartButton="定期購入ボタン", inventoryDisplay="在庫数表示", lowStockThreshold="残り在庫数表示閾値", shopContact="商品問い合わせボタン", review="レビュー本文表示", displayManufacturerContents="メーカー提供情報表示"))
    #アクセスコントロール
    #accessControl = models.JSONField(default=dict(taxIncluded="消費税込み", taxRate="消費税税率", cashOnDeliveryFeeIncluded="代引料"))
    #決済情報
    # payment = models.JSONField(default=dict(taxIncluded= "消費税込み", taxRate="消費税税率", cashOnDeliveryFeeIncluded= "代引料"))
    #ポイント変倍情報
    #pointCampaign = models.JSONField(default=dict(applicablePeriod=dict(start= "開始日時", end= "終了日時"), benefits=dict(pointRate= "ポイント変倍率"), optimization=dict(maxPointRate= "ポイント上限倍率")))
    #店舗内カテゴリでの表示順位
    # itemDisplaySequence = models.IntegerField()
    #レイアウト設定
    # layout = models.JSONField(default=dict(itemLayoutId= "商品ページレイアウト", navigationId="ヘッダー・フッター・レフトナビのテンプレートID", layoutSequenceId="表示項目の並び順テンプレートID", smallDescriptionId="共通説明文(小)テンプレートID", largeDescriptionId="共通説明文(大)テンプレートID", showcaseId="目玉商品テンプレートID"))
    #バリエーション項目
    #variantSelectors = models.JSONField(default=dict(key="バリエーション項目キー", displayName="バリエーション項目名", values=[dict(displayValue= "バリエーション選択肢")]))
    #登録日時
    # created = models.DateField()
    #更新日時
    # updated = models.DateField()
    #廃番？
    # is_deleted = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #関係
    item = models.ForeignKey(ItemItem, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.manageNumber

class Sku(models.Model):
    #sku管理番号
    variantId = models.CharField(max_length=255, blank=True, db_index=True)
    #システム連携用SKU番号
    #merchantDefinedSkuId = models.CharField(blank=True)
    #SKU情報
    #selectorValues = models.JSONField(default=dict(key=None))
    #SKU画像
    #images = models.JSONField(default=dict(images=[dict(type= "SKU画像タイプ", location= "SKU画像パス", alt= "SKU画像名（ALT）")]))
    #在庫戻しフラグ
    #restockOnCancel = models.CharField(blank=True)
    #在庫切れ時の注文受付
    #backOrderFlag = models.CharField(blank=True)
    #在庫あり時納期管理番号
    #normalDeliveryDateId = models.IntegerField(blank=True)
    #在庫切れ時納期管理番号
    #backOrderDeliveryDateId = models.IntegerField(blank=True)
    #注文受付数
    #orderQuantityLimit = models.IntegerField(blank=True)
    #表示価格情報
    referencePrice = models.JSONField(default=dict(displayType="表示価格種別", type="表示価格文言", value="表示価格"))
    #その他設定
    #features = models.JSONField(default=dict(restockNotification="再入荷お知らせボタン", noshi="のし対応"))
    #SKU倉庫設定
    #hidden = models.CharField(blank=True)
    #販売価格
    standardPrice = models.IntegerField(blank=True)
    #定期購入販売価格設定
    #subscriptionPrice = models.JSONField(default=dict(basePrice="定期購入販売価格", individualPrices=dict(firstPrice="初回価格")))
    #セット商品用カタログID
    #articleNumberForSet = models.JSONField(blank=True)
    #カタログID情報
    #articleNumber = models.JSONField(default=dict(value="カタログID", exemptionReason="カタログIDなしの理由"))
    #送料情報
    #shipping = models.JSONField(default=dict(fee="個別送料", postageIncluded="送料無料フラグ", shopAreaSoryoPatternId="地域別個別送料管理番号", shippingMethodGroup="配送方法セット管理番号", postageSegment=dict(local= "送料区分1（ローカル）", overseas= "送料区分2（海外）"), overseasDeliveryId="海外配送管理番号", singleItemShipping="単品配送設定"))
    #属性情報自由入力行
    #specs = models.JSONField(default=dict(specs=[dict(label="属性情報自由入力行（項目）", value="属性情報自由入力行（値）")]))
    #属性情報
    #attributes = models.JSONField(default=dict(attributes=[dict(name="属性情報名", values="属性情報（実値）", unit= "単位")]))
    #廃番？
    # is_deleted = models.BooleanField(default=False)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #関係
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return self.variantId

class Record(models.Model):
    shop_name = models.CharField()
    price = models.IntegerField()
    our_price = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    pass
"""
class RakutenCoordiroomItem(models.Model):
    #商品管理番号
    manageNumber = models.CharField()
    #商品番号
    itemNumber = models.CharField(max_length=255, blank=True)
    #商品名
    title = models.CharField()
    #キャッチコピー
    tagline = models.CharField(blank=True)
    #商品説明文
    productDescription = models.JSONField(default=dict(pc="PC要商品説明文", sp="スマートフォン要商品説明文"))
    #PC用販売説明文
    salesDescription = models.TextField(blank=True)
    #医薬品説明文・注意事項
    precautions = models.JSONField(default = dict(description= "医薬品説明文", agreement= "医療品注意事項"))
    #商品種別
    itemType = models.CharField(choices=[("NORMAL", "通常商品"), ("PRE_ORDER", "予約商品"), ("SUBSCRIPTION", "定期購入商品")])
    #商品画像
    images = models.JSONField(default=dict(images=[dict(type="商品画像種別",location="商品画像種別",alt="商品画像名（ALT）")]))
    #白背景画像
    whiteBgImage = models.JSONField(default=dict(type= "白背景画像種別", location= "白背景画像URL"))
    #動画
    video = models.JSONField(default=dict(type= "動画種別", parameters= dict(value= "動画のURL")))
    #ジャンルID
    genreId = models.CharField()
    #非製品属性タグID
    tags = models.JSONField(default=dict(tags= []))
    #倉庫指定
    hideItem = models.BooleanField()
    #在庫設定なし
    unlimitedInventoryFlag = models.BooleanField()
    #商品オプション（項目選択肢）
    customizationOptions = models.JSONField(default=dict(customizationOptions= [dict(displayName= "商品オプション（項目選択肢）項目名", inputType= "商品オプション選択肢タイプ", required= "商品オプション必須フラグ", selections= [dict(displayValue= "商品オプション選択肢名")])]))
    #予約商品発売日
    releaseDate = models.DateField(blank=True)
    #販売期間指定
    purchasablePeriod = models.JSONField(default=dict(start="販売開始日時", end="販売終了日時"))
    #定期購入商品設定
    subscription = models.JSONField(default=dict(shippingDateFlag= "お届け日付指定フラグ", shippingIntervalFlag= "お届け間隔指定フラグ"))
    #その他設定
    features = models.JSONField(default=dict(searchVisiblity= "サーチ表示", displayNormalCartButton= "注文ボタン", displaySubscriptionCartButton="定期購入ボタン", inventoryDisplay="在庫数表示", lowStockThreshold="残り在庫数表示閾値", shopContact="商品問い合わせボタン", review="レビュー本文表示", displayManufacturerContents="メーカー提供情報表示"))
    #アクセスコントロール
    accessControl = models.JSONField(default=dict(taxIncluded="消費税込み", taxRate="消費税税率", cashOnDeliveryFeeIncluded="代引料"))
    #決済情報
    payment = models.JSONField(default=dict(taxIncluded= "消費税込み", taxRate="消費税税率", cashOnDeliveryFeeIncluded= "代引料"))
    #ポイント変倍情報
    pointCampaign = models.JSONField(default=dict(applicablePeriod=dict(start= "開始日時", end= "終了日時"), benefits=dict(pointRate= "ポイント変倍率"), optimization=dict(maxPointRate= "ポイント上限倍率")))
    #店舗内カテゴリでの表示順位
    itemDisplaySequence = models.IntegerField()
    #レイアウト設定
    layout = models.JSONField(default=dict(itemLayoutId= "商品ページレイアウト", navigationId="ヘッダー・フッター・レフトナビのテンプレートID", layoutSequenceId="表示項目の並び順テンプレートID", smallDescriptionId="共通説明文(小)テンプレートID", largeDescriptionId="共通説明文(大)テンプレートID", showcaseId="目玉商品テンプレートID"))
    #バリエーション項目
    variantSelectors = models.JSONField(default=dict(key="バリエーション項目キー", displayName="バリエーション項目名", values=[dict(displayValue= "バリエーション選択肢")]))
    #登録日時
    created = models.DateField()
    #更新日時
    updated = models.DateField()
    #廃番？
    is_deleted = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #関係
    item = models.ForeignKey(item.models.Item, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.manageNumber

class RakutenCoordiroomSku(models.Model):
    #sku管理番号
    variantId = models.CharField(max_length=255, blank=True, db_index=True)
    #システム連携用SKU番号
    merchantDefinedSkuId = models.CharField(blank=True)
    #SKU情報
    selectorValues = models.JSONField(default=dict(key=None))
    #SKU画像
    images = models.JSONField(default=dict(images=[dict(type= "SKU画像タイプ", location= "SKU画像パス", alt= "SKU画像名（ALT）")]))
    #在庫戻しフラグ
    restockOnCancel = models.CharField(blank=True)
    #在庫切れ時の注文受付
    backOrderFlag = models.CharField(blank=True)
    #在庫あり時納期管理番号
    normalDeliveryDateId = models.IntegerField(blank=True)
    #在庫切れ時納期管理番号
    backOrderDeliveryDateId = models.IntegerField(blank=True)
    #注文受付数
    orderQuantityLimit = models.IntegerField(blank=True)
    #表示価格情報
    referencePrice = models.JSONField(default=dict(displayType="表示価格種別", type="表示価格文言", value="表示価格"))
    #その他設定
    features = models.JSONField(default=dict(restockNotification="再入荷お知らせボタン", noshi="のし対応"))
    #SKU倉庫設定
    hidden = models.CharField(blank=True)
    #販売価格
    standardPrice = models.IntegerField(blank=True)
    #定期購入販売価格設定
    subscriptionPrice = models.JSONField(default=dict(basePrice="定期購入販売価格", individualPrices=dict(firstPrice="初回価格")))
    #セット商品用カタログID
    articleNumberForSet = models.JSONField(blank=True)
    #カタログID情報
    articleNumber = models.JSONField(default=dict(value="カタログID", exemptionReason="カタログIDなしの理由"))
    #送料情報
    shipping = models.JSONField(default=dict(fee="個別送料", postageIncluded="送料無料フラグ", shopAreaSoryoPatternId="地域別個別送料管理番号", shippingMethodGroup="配送方法セット管理番号", postageSegment=dict(local= "送料区分1（ローカル）", overseas= "送料区分2（海外）"), overseasDeliveryId="海外配送管理番号", singleItemShipping="単品配送設定"))
    #属性情報自由入力行
    specs = models.JSONField(default=dict(specs=[dict(label="属性情報自由入力行（項目）", value="属性情報自由入力行（値）")]))
    #属性情報
    attributes = models.JSONField(default=dict(attributes=[dict(name="属性情報名", values="属性情報（実値）", unit= "単位")]))
    #廃番？
    is_deleted = models.BooleanField(default=False)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #関係
    item = models.ForeignKey(RakutenMaidoItem, on_delete=models.CASCADE)
    def __str__(self):
        return self.variantId
"""