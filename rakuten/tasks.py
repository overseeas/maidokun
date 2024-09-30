from .models import Item, Sku

from datetime import datetime
from . import api
from celery import shared_task

@shared_task
def test_task():
    print("start2")
    try:
        had = "test"
        dry = had/1
        print("end")
    except:
        print("error")

@shared_task
def recently_updated(last_update=False):
    print("update start")
    if not(last_update):
        last_update = Item.objects.order_by("-updated_at").first().updated_at
        #last_update = datetime.strptime("1999-01-01T01:00:00+09:00", '%Y-%m-%dT%H:%M:%S%z')
    print(last_update)
    items = get_updated_list(last_update)
    for item in items:
        if not(Item.objects.filter(manage_number= item["manageNumber"]).exists()):
            Item.objects.create(manage_number= item["manageNumber"], title=item["title"], updated_at = item["updated"])
        Item.objects.filter(manage_number= item["manageNumber"]).update(
            hide_item=item["hideItem"],
            updated_at = item["updated"],
        )

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
    return True


def get_updated_list(limit_time):
    cursorMark = ""
    next_cursorMark = "*"
    updated_items = []

    while cursorMark != next_cursorMark:
        cursorMark = next_cursorMark
        response = api.items_search({"hits": "100", "cursorMark": cursorMark})
        for item in response["results"]:
            print(item["item"]["manageNumber"])
            #"2024-09-11T15:12:48+09:00"
            updated = datetime.strptime(item["item"]["updated"], '%Y-%m-%dT%H:%M:%S%z')
            if updated < limit_time:
                #print("function end")
                return updated_items
            updated_items.append(item["item"])
        next_cursorMark = response["nextCursorMark"]
    return updated_items