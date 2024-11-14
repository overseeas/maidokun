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
    #医療品説明文
    precautions_description = models.TextField(null=True)
    #医療品注意事項
    precautions_agreement = models.TextField(null=True)
    #商品種別
    itemType = models.CharField(null=True)
    #白背景画像種別
    whiteBgImage_type = models.CharField(null=True)
    #白背景画像URL
    whiteBgImage_location = models.URLField(null=True)
    #動画種別
    video_type = models.TextField(null=True)
    #動画のURL
    video_parameters_value = models.URLField(null=True)
    #ジャンルID
    genreId = models.CharField(null=True)
    #非製品属性タグID
    tags = models.CharField(null=True)
    #倉庫指定
    hideItem = models.CharField(null=True)
    #在庫設定なし
    unlimitedInventoryFlag = models.CharField(null=True)
    #予約商品発売日
    releaseDate = models.DateField(null=True)
    #販売開始日時
    purchasablePeriod_start = models.DateTimeField(null=True)
    #販売終了日時
    purchasablePeriod_end = models.DateTimeField(null=True)
    #お届け日付指定フラグ
    subscription_shippingDateFlag = models.CharField(null=True)
    #お届け間隔指定フラグ
    subscription_shippingIntervalFlag = models.CharField(null=True)
    #サーチ表示
    features_searchVisibility = models.CharField(null=True)
    #注文ボタン
    features_displayNormalCartButton = models.CharField(null=True)
    #定期購入ボタン
    features_displaySubscriptionCartButton = models.CharField(null=True)
    #在庫表表示
    features_inventoryDisplay = models.CharField(null=True)
    #残り在庫数表示閾値
    features_lowStockThreshold = models.CharField(null=True)
    #商品問い合わせボタン
    features_shopContact = models.CharField(null=True)
    #レビュー本文表示
    features_review = models.CharField(null=True)
    #メーカー提供情報表示
    features_displayManufacturerContents = models.CharField(null=True)
    #闇市パスワード
    accessControl_accessPassword = models.CharField(null=True)
    #消費税込み
    payment_taxIncluded = models.CharField(null=True)
    #消費税税率
    payment_taxRate = models.CharField(null=True)
    #代引料
    payment_cashOnDeliveryFeeIncluded = models.CharField(null=True)
    #ポイント変倍適用期間_	開始日時
    pointCampaign_applicablePeriod_start = models.DateTimeField(null=True)
    #ポイント変倍適用期間_	終了日時
    pointCampaign_applicablePeriod_end = models.DateTimeField(null=True)
    #ポイント変倍率
    pointCampaign_benefits_pointRate = models.IntegerField(null=True)
    #ポイント上限倍率
    pointCampaign_optimization_maxPointRate = models.IntegerField(null=True)
    #店舗内カテゴリでの表示順位
    itemDisplaySequence = models.IntegerField(null=True)
    #商品ページレイアウト
    layout_itemLayoutId = models.IntegerField(null=True)
    #ヘッダー・フッター・レフトナビのテンプレートID
    layout_navigationId = models.IntegerField(null=True)
    #表示項目の並び順テンプレートID
    layout_layoutSequenceId = models.IntegerField(null=True)
    #共通説明文(小)テンプレートID
    layout_smallDescriptionId = models.IntegerField(null=True)
    #共通説明文(大)テンプレートID
    layout_largeDescriptionId = models.IntegerField(null=True)
    #目玉商品テンプレートID
    layout_showcaseId = models.IntegerField(null=True)

    review_count = models.IntegerField(null=True)
    review_avarageRating = models.FloatField(null=True)

    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.manageNumber


class Sku(models.Model):
    #sku管理番号
    skuNumber = models.CharField(max_length=255, null=True, db_index=True)
    #システム連携用SKU番号
    merchantDefinedSkuId = models.CharField(null=True)
    #在庫戻しフラグ
    restockOnCancel = models.CharField(null=True)
    #在庫切れ時の注文受付
    backOrderFlag = models.CharField(null=True)
    #在庫あり時納期管理番号
    normalDeliveryDateId = models.IntegerField(null=True)
    #在庫切れ時納期管理番号
    backOrderDeliveryDateId = models.IntegerField(null=True)
    #注文受付数
    orderQuantityLimit = models.IntegerField(null=True)
    #表示価格種別
    referencePrice_displayType = models.CharField(max_length=255, null=True)
    #表示価格
    referencePrice_value = models.CharField(null=True)
    #再入荷お知らせボタン
    features_restockNotification = models.CharField(null=True)
    #のし対応
    featrues_noshi = models.CharField(null=True)
    #SKU倉庫設定
    hidden = models.CharField(null=True)
    #販売価格
    standardPrice = models.IntegerField(null=True)
    #定期購入販売価格
    subscriptionPrice_basePrice = models.CharField(null=True)
    #個別価格
    subscriptionPrice_individualPrices_firstPrice = models.CharField(null=True)
    #カタログID
    articleNumber_value = models.CharField(null=True)
    #カタログIDなしの理由
    articleNumber_exemptionReason = models.CharField(null=True)
    #個別送料
    shipping_fee = models.CharField(null=True)
    #送料無料フラグ
    shipping_postageIncluded = models.CharField(null=True)
    #地域別個別送料管理番号
    shipping_shopAreaSoryoPatternId = models.IntegerField(null=True)
    #配送方法セット管理番号
    shipping_shippingMethodGroup = models.CharField(null=True)
    #送料区分1（ローカル）
    shipping_postageSegment_local = models.IntegerField(null=True)
    #送料区分2（海外）
    shipping_postageSegment_overseas = models.IntegerField(null=True)
    #海外配送管理番号
    shipping_overseasDeliveryId = models.IntegerField(null=True)
    #単品配送設定
    shipping_singleItemShipping = models.IntegerField(null=True)


    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=True)

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return self.skuNumber