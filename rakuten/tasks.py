from .models import Item, Sku

from datetime import datetime
from . import api
from celery import shared_task


@shared_task
def recently_updated(last_update="1900-01-01T12:40:29+09:00"):
    print("start")
    items = get_updated_list(last_update)
    for item in items:
        if not(Item.objects.filter(manage_number= item["manageNumber"]).exists()):
            Item.objects.create(manage_number= item["manageNumber"], title=item["title"])
        Item.objects.filter(manage_number= item["manageNumber"]).update(hide_item=item["hideItem"])

        skus = item["variants"]
        for sku, detail in skus.items():
            if not(Sku.objects.filter(sku_number=sku).exists()):
                Sku.objects.create(sku_number=sku, item= Item.objects.get(manage_number=item["manageNumber"]))
            
            #reference_price
            try:
                if "value" in detail["referencePrice"]:
                    reference_price = detail["referencePrice"]["value"]
                else:
                    reference_price = detail["referencePrice"]["displayType"]

                Sku.objects.filter(sku_number=sku).update(
                    standard_price= detail["standardPrice"],
                    reference_price= reference_price,
                    hidden= detail["hidden"],
                )
            except:
                print(sku)
    print("end")
    return True

@shared_task
def get_updated_list(limit_time):
    print("function start")
    cursorMark = ""
    next_cursorMark = "*"
    updated_items = []

    while cursorMark != next_cursorMark:
        cursorMark = next_cursorMark
        response = api.items_search({"hits": "100", "cursorMark": cursorMark})
        for item in response["results"]:
            #"2024-09-11T15:12:48+09:00"
            updated = datetime.strptime(item["item"]["updated"], '%Y-%m-%dT%H:%M:%S%z')
            if updated < limit_time:
                #print("function end")
                return updated_items
            updated_items.append(item["item"])
        next_cursorMark = response["nextCursorMark"]
    print("function end")
    return updated_items