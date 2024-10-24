from django.http import StreamingHttpResponse
from .models import Item, Sku

import csv
from itertools import chain

class FieldName:
    def __init__(self, names):
        # Item field
        # Sku field
        if "SKU管理番号" in names: self.skuNumber = "SKU管理番号"
        if "表示価格種別" in names: self.referencePrice_displayType = "表示価格種別"
        if "表示価格" in names: self.referencePrice_value = "表示価格"
        if "SKU倉庫設定" in names: self.hidden = "SKU倉庫設定"
        if "販売価格" in names: self.standardPrice = "販売価格"
        if "カタログID" in names: self.articleNumber_value = "カタログID"
        if "カタログIDなしの理由" in names: self.articleNumber_exemptionReason = "カタログIDなしの理由"



class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def all_data_for_vlookup(request):
    # set field name
    fields_name = FieldName()
    fields_name.skuNumber = "SKU管理番号"
    fields_name.referencePrice_displayType = "表示価格種別"
    fields_name.referencePrice_value = "表示価格"
    fields_name.hidden = "SKU倉庫設定"
    fields_name.standardPrice = "販売価格"
    fields_name.articleNumber_value = "カタログID"
    fields_name.articleNumber_exemptionReason = "カタログIDなしの理由"


    rows = Sku.objects.all()
    rows = list(chain([fields_name], rows))
    print(rows[0])
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    return StreamingHttpResponse(
        (writer.writerow([row.skuNumber, row.referencePrice_value]) for row in rows),
        content_type="text/csv; charset=shift-jis",
        headers={"Content-Disposition": 'attachment; filename="sku.csv"'},
    )