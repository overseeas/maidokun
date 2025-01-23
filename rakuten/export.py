from django.http import StreamingHttpResponse, HttpResponse
from .models import Item, Sku

import csv
from itertools import chain

class ItemField():
    def __init__(self):
        self.manageNumber = "商品管理番号"
        self.itemNumber = "商品番号"
        self.title = "商品名"
        self.tagline = "キャッチコピー"
        self.productDescription_pc = "PC用商品説明文"
        self.productDescription_sp = "スマートフォン用商品説明文"
        self.salesDescription = "PC用販売説明文"
        self.itemType = "商品種別"
        self.genreId = "ジャンルID"
        self.tags = "非製品属性タグID"
        self.hideItem = "倉庫指定"
        self.features_searchVisibility = "サーチ表示"
        self.features_displayNormalCartButton = "注文ボタン表示"
        self.features_inventoryDisplay = "在庫表表示"
        self.features_shopContact = "お問い合わせボタン表示"
        self.payment_taxIncluded = "消費税込み"
        self.payment_cashOnDeliveryFeeIncluded = "代引料"
        self.controlColumn = "コントロールカラム"

class SkuField:
    def __init__(self):
        # item
        self.item = ItemField()

        # sku
        self.skuNumber = "SKU管理番号"
        self.referencePrice_displayType = "表示価格種別"
        self.referencePrice_value = "表示価格"
        self.hidden = "SKU倉庫設定"
        self.standardPrice = "販売価格"
        self.articleNumber_value = "カタログID"
        self.articleNumber_exemptionReason = "カタログIDなしの理由"
        self.shipping_postageIncluded = "送料"
        self.normalDeliveryDateId = "在庫あり時納期管理番号"
        self.shipping_shippingMethodGroup = "配送方法セット管理番号"



class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def all_data_for_vlookup(request):
    rows = []
    # set field name
    fields_name = SkuField()
    rows = Sku.objects.filter(is_deleted= False)

    rows = list(chain([fields_name], rows))
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    return StreamingHttpResponse(
        (writer.writerow([
            row.item.controlColumn, 
            row.item.manageNumber, 
            row.item.title, 
            row.standardPrice, 
            row.referencePrice_value, 
            row.shipping_postageIncluded, 
            row.hidden, 
            row.shipping_shippingMethodGroup,
            row.skuNumber, 
            row.item.hideItem,
            row.normalDeliveryDateId,
            ]) for row in rows),
        content_type="text/csv; charset=utf_8_sig",
        headers={"Content-Disposition": 'attachment; filename="data.csv"'},
    )