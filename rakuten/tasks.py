from .models import Item, Sku

from datetime import datetime
from . import api
from celery import shared_task


@shared_task
def recently_updated(last_update=False):
    if not(last_update):
        last_update = Item.objects.order_by("-updated_at").first().updated_at
        #last_update = datetime.strptime("1999-01-01T01:00:00+09:00", '%Y-%m-%dT%H:%M:%S%z')
    print(last_update)
    items = get_updated_list(last_update)
    for item in items:
        #商品
        if not(Item.objects.filter(manageNumber= item["manageNumber"]).exists()):
            Item.objects.create(manageNumber= item["manageNumber"], updated_at = item["updated"])
        args_updated = dict(updated_at = item["updated"])


        if "itemNumber" in item: args_updated["itemNumber"] = item["itemNumber"]
        if "title" in item: args_updated["title"] = item["title"]
        if "tagline" in item["tagline"]: args_updated["tagline"] = item["tagline"]
        if "productDescription" in item:
            if "pc" in item["productDescription"]: args_updated["productDescription_pc"] = item["productDescription"]["pc"]
            if "sp" in item["productDescription"]: args_updated["productDescription_sp"] = item["productDescription"]["sp"]
        if "salesDescription" in item: args_updated["salesDescription"] = item["salesDescription"]
        if "itemType" in item: args_updated["itemType"] = item["itemType"]
        if "genreId" in item: args_updated["genreId"] = item["genreId"]
        if "tags" in item: args_updated["tags"] = item["tags"]
        if "hideItem" in item: args_updated["hideItem"] = item["hideItem"]
        if "features" in item:
            if "searchVisibility" in item["features"]: args_updated["features_searchVisibility"] = item["features"]["searchVisibility"]
            if "shopContact" in item["features"]: args_updated["features_shopContact"] = item["features"]["shopContact"]
            if "displayNormalCartButton" in item["features"]: args_updated["features_displayNormalCartButton"] = item["features"]["displayNormalCartButton"]
            if "inventoryDisplay" in item["features"]: args_updated["features_inventoryDisplay"] = item["features"]["inventoryDisplay"]
        if "payment" in item:
            if "taxIncluded" in item["payment"]: args_updated["payment_taxIncluded"] = item["payment"]["taxIncluded"]
            if "cashOnDeliveryFeeIncluded" in item["payment"]: args_updated["payment_cashOnDeliveryFeeIncluded"] = item["payment"]["cashOnDeliveryFeeIncluded"]

        Item.objects.filter(manageNumber= item["manageNumber"]).update(**args_updated)

        skus = item["variants"]
        #SKU
        for sku, detail in skus.items():
            if not(Sku.objects.filter(skuNumber=sku).exists()):
                Sku.objects.create(skuNumber=sku, item= Item.objects.get(manageNumber=item["manageNumber"]))

            sku_args_updated = dict()
            if "standardPrice" in detail: sku_args_updated["standardPrice"] = detail["standardPrice"]
            if "referencePrice" in detail:
                if "displayType" in detail["referencePrice"]: sku_args_updated["referencePrice_value"] = detail["referencePrice"]["value"]
                if "value" in detail["referencePrice"]: sku_args_updated["referencePrice_value"] = detail["referencePrice"]["value"]
            if "hidden" in detail: sku_args_updated["hidden"] = detail["hidden"]
            if "articleNumber":
                if "value" in detail["articleNumber"]: sku_args_updated["articleNumber_value"] = detail["articleNumber"]["value"]
                if "exemptionReason" in detail["articleNumber"]: sku_args_updated["articleNumber_exemptionReason"] = detail["articleNumber"]["exemptionReason"]


            Sku.objects.filter(skuNumber=sku).update(**sku_args_updated)
    return True


def get_updated_list(limit_time):
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
                return updated_items
            updated_items.append(item["item"])
        next_cursorMark = response["nextCursorMark"]
    return updated_items