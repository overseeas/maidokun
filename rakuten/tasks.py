from .models import RakutenMaidoItem, RakutenMaidoSku
from django.http import HttpResponse
from django.utils.timezone import make_aware

from datetime import datetime
from . import api
from celery import shared_task



@shared_task
def recently_updated(last_update=False):
    #last_update_to_show = datetime.strftime(datetime.now(), '%Y-%m-%dT%H:%M:%S%z')
    last_update_to_show = make_aware(datetime.now())
    if not(last_update):
        last_update = RakutenMaidoItem.objects.order_by("-updated_at").first().updated_at
        #last_update = datetime.strptime("1999-01-01T01:00:00+09:00", '%Y-%m-%dT%H:%M:%S%z')
    print(last_update)
    print(last_update_to_show)
    items = get_updated_list(last_update)
    print("retrieved datas from rms")
    for item in items:
        try:
            #商品
            if not(RakutenMaidoItem.objects.filter(manageNumber= item["manageNumber"]).exists()):
                RakutenMaidoItem.objects.create(manageNumber= item["manageNumber"], updated_at = item["updated"])
            args_updated = dict(updated_at = item["updated"])

            if "title" in item: args_updated["title"] = item["title"]
            if "hideItem" in item: 
                if item["hideItem"] == True:
                    args_updated["hideItem"] = "1"
                else:
                    args_updated["hideItem"] = "0"
            if "features" in item:
                if "searchVisibility" in item["features"]: args_updated["features_searchVisibility"] = item["features"]["searchVisibility"]
                if "shopContact" in item["features"]: args_updated["features_shopContact"] = item["features"]["shopContact"]
                if "displayNormalCartButton" in item["features"]: args_updated["features_displayNormalCartButton"] = item["features"]["displayNormalCartButton"]
                if "inventoryDisplay" in item["features"]: args_updated["features_inventoryDisplay"] = item["features"]["inventoryDisplay"]
            if "payment" in item:
                if "taxIncluded" in item["payment"]: args_updated["payment_taxIncluded"] = item["payment"]["taxIncluded"]
                if "cashOnDeliveryFeeIncluded" in item["payment"]: args_updated["payment_cashOnDeliveryFeeIncluded"] = item["payment"]["cashOnDeliveryFeeIncluded"]

            RakutenMaidoItem.objects.filter(manageNumber= item["manageNumber"]).update(**args_updated)

            skus = item["variants"]
            #SKU
            for sku, detail in skus.items():
                if not(RakutenMaidoSku.objects.filter(skuNumber=sku).exists()):
                    RakutenMaidoSku.objects.create(skuNumber=sku, item= RakutenMaidoItem.objects.get(manageNumber=item["manageNumber"]))

                sku_args_updated = dict(updated_at = last_update_to_show)

                if "normalDeliveryDateId" in detail: sku_args_updated["normalDeliveryDateId"] = detail["normalDeliveryDateId"]
                if "standardPrice" in detail: sku_args_updated["standardPrice"] = detail["standardPrice"]
                if "referencePrice" in detail:
                    if "displayType" in detail["referencePrice"]:
                        sku_args_updated["referencePrice_displayType"] = detail["referencePrice"]["displayType"]
                        if detail["referencePrice"]["displayType"] == "OPEN_PRICE":
                            sku_args_updated["referencePrice_value"] = "open"
                        elif detail["referencePrice"]["displayType"] == "SHOP_SETTING":
                            if "value" in detail["referencePrice"]:
                                sku_args_updated["referencePrice_value"] = detail["referencePrice"]["value"]
                if "hidden" in detail: 
                    if detail["hidden"] == True:
                        sku_args_updated["hidden"] = 1
                    else:
                        sku_args_updated["hidden"] = 0
                if "shipping" in detail:
                    if "shippingMethodGroup" in detail["shipping"]: sku_args_updated["shipping_shippingMethodGroup"] = detail["shipping"]["shippingMethodGroup"]
                    if "postageIncluded" in detail["shipping"]: 
                        if detail["shipping"]["postageIncluded"] == True:
                            sku_args_updated["shipping_postageIncluded"] = "1"
                        else:
                            sku_args_updated["shipping_postageIncluded"] = "0"
                RakutenMaidoSku.objects.filter(skuNumber=sku).update(**sku_args_updated)
        except:
            print(item["manageNumber"])
    print("Done")
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

def get_manageNumber_only():
    cursorMark = ""
    next_cursorMark = "*"
    updated_items = []

    while cursorMark != next_cursorMark:
        cursorMark = next_cursorMark
        response = api.items_search({"hits": "100", "cursorMark": cursorMark})
        for item in response["results"]:
            updated_items.append(item["item"]["manageNumber"])
        next_cursorMark = response["nextCursorMark"]
    return updated_items

@shared_task
def update_all():
    date = datetime.strptime("1999-01-01T01:00:00+09:00", '%Y-%m-%dT%H:%M:%S%z')
    #date = datetime.strptime("2024-11-21T15:00:00+09:00", '%Y-%m-%dT%H:%M:%S%z')
    items = get_updated_list(date)
    print("retrieved datas from rms")

    for item in items:
        try:
            #商品
            if not(RakutenMaidoItem.objects.filter(manageNumber= item["manageNumber"]).exists()):
                RakutenMaidoItem.objects.create(manageNumber= item["manageNumber"], updated_at = item["updated"])
            args_updated = dict(updated_at = item["updated"])

            if "title" in item: args_updated["title"] = item["title"]
            if "hideItem" in item: 
                if item["hideItem"] == True:
                    args_updated["hideItem"] = "1"
                else:
                    args_updated["hideItem"] = "0"
            if "features" in item:
                if "searchVisibility" in item["features"]: args_updated["features_searchVisibility"] = item["features"]["searchVisibility"]
                if "shopContact" in item["features"]: args_updated["features_shopContact"] = item["features"]["shopContact"]
                if "displayNormalCartButton" in item["features"]: args_updated["features_displayNormalCartButton"] = item["features"]["displayNormalCartButton"]
                if "inventoryDisplay" in item["features"]: args_updated["features_inventoryDisplay"] = item["features"]["inventoryDisplay"]
            if "payment" in item:
                if "taxIncluded" in item["payment"]: args_updated["payment_taxIncluded"] = item["payment"]["taxIncluded"]
                if "cashOnDeliveryFeeIncluded" in item["payment"]: args_updated["payment_cashOnDeliveryFeeIncluded"] = item["payment"]["cashOnDeliveryFeeIncluded"]

            RakutenMaidoItem.objects.filter(manageNumber= item["manageNumber"]).update(**args_updated)

            skus = item["variants"]
            #SKU
            for sku, detail in skus.items():
                if not(RakutenMaidoSku.objects.filter(skuNumber=sku).exists()):
                    RakutenMaidoSku.objects.create(skuNumber=sku, item= RakutenMaidoItem.objects.get(manageNumber=item["manageNumber"]))

                sku_args_updated = dict()

                if "normalDeliveryDateId" in detail: sku_args_updated["normalDeliveryDateId"] = detail["normalDeliveryDateId"]
                if "standardPrice" in detail: sku_args_updated["standardPrice"] = detail["standardPrice"]
                if "referencePrice" in detail:
                    if "displayType" in detail["referencePrice"]:
                        sku_args_updated["referencePrice_displayType"] = detail["referencePrice"]["displayType"]
                        if detail["referencePrice"]["displayType"] == "OPEN_PRICE":
                            sku_args_updated["referencePrice_value"] = "open"
                        elif detail["referencePrice"]["displayType"] == "SHOP_SETTING":
                            if "value" in detail["referencePrice"]:
                                sku_args_updated["referencePrice_value"] = detail["referencePrice"]["value"]
                if "hidden" in detail: 
                    if detail["hidden"] == True:
                        sku_args_updated["hidden"] = 1
                    else:
                        sku_args_updated["hidden"] = 0
                if "shipping" in detail:
                    if "shippingMethodGroup" in detail["shipping"]: sku_args_updated["shipping_shippingMethodGroup"] = detail["shipping"]["shippingMethodGroup"]
                    if "postageIncluded" in detail["shipping"]: 
                        if detail["shipping"]["postageIncluded"] == True:
                            sku_args_updated["shipping_postageIncluded"] = "1"
                        else:
                            sku_args_updated["shipping_postageIncluded"] = "0"
                RakutenMaidoSku.objects.filter(skuNumber=sku).update(**sku_args_updated)
        except:
            print(item["manageNumber"])
    return True

@shared_task
def retrieve_deleted_items():
    items = get_manageNumber_only()
    itemobjs = RakutenMaidoItem.objects.filter(is_deleted= False)
    print("retrieved datas from rms")
    
    for itemobj in itemobjs:
        if itemobj.manageNumber not in items:
            print(itemobj.manageNumber)
            itemobj.is_deleted = True 
            itemobj.save()
    
    for deleted_item in RakutenMaidoItem.objects.filter(is_deleted= True):
        RakutenMaidoSku.objects.filter(item=deleted_item.id).update(is_deleted= True)

    return True

def drop_items():
    targets = ["T382639","T382638","T382635","T382637","T382636","T382633","T382630","T382629","T382634","T382631","T382632","T382611","T382606","T382612","T382604","T382605","T382609","T382610","T382607","T382596","T382601","T382608","T382597","T382603","T382600","T382602","T382598","T382599","T382595","T382593","T382592","T382589","T382591","T382594","T382622","T382590","T382621","T382625","T382587","T382628","T382585","T382588","T382624","T382626","T382582","T382623","T382571","T382579","T382581","T382584","T382562","T382586","T382568","T382570","T382620","T382564","T382578","T382577","T382580","T382618","T382567","T382569","T382617","T382563","T382565","T382572","T382614","T382680","T382615","T382619","T382613","T382566","T382677","T382616","T382675","T382678","T382681","T382683","T382684","T382682","T382666","T382663","T382676","T382673","T382679","T382672","T382667","T382668","T382674","T382670","T382669","T382665","T382662","T382671","T382656","T382659","T382664","T382661","T382660","T382657","T382576","T382658","T382654","T382652","T382646","T382643","T382644","T382573","T382653","T382575","T382642","T382655","T382650","T382627","T382649","T382645","T382647","T382651","T382648","T382641","T382574","T382561","T382583","T382640"]

    for target in targets:
        RakutenMaidoSku.objects.get(skuNumber= target).delete()

def dropped_items():
    targets = ["nyt2104","nyt2103","nys35245le2","nyt2102","nys35255le2","nys35215le2","nys35135le9","nys35115le9","nys35235le2","nys35145le9","nys35155le9","nys15370kle9","nys15271kle9","nys15371kle9","nys15243kle9","nys15270kle9","nys15342kle9","nys15343kle9","nys15340kle9","nys15141kle9","nys15240kle9","nys15341kle9","nys15142kle9","nys15242kle9","nys15171kle9","nys15241kle9","nys15143kle9","nys15170kle9","nys15140kle9","nys15070kle7","nys15043kle7","nys15040kle7","nys15042kle7","nys15071kle7","nts90551dd9","nys15041kle7","nts90355dd9","nyk43055","nny20398le7","nyk43066","nny20393le7","nny20399le7","nyk43015","nyk43056","nny20374le1","nyk43010lf2","nncf42735le9","nny20358le1","nny20373le1","nny20379le1","nnlg48117","nny20394le7","nncf42255le9","nncf42655le9","nncf22735le9","nnlg48330","nny20354le1","nny20353le1","nny20359le1","nncf22635le9","nncf42235le9","nncf42635le9","nncf22615le9","nnlg48123","nncf42135le9","nncf42755le9","nncf22135le9","fk80011","nncf22215le9","nncf22715le9","nncf22115le9","nncf42155le9","fk792","nncf22235le9","fk763","fk793","fk80012","fp02091c","fw90032c","fk80013","fk709","fk705","fk764p","fk760p","fk80010","fk758","fk722","fk723","fk762","fk752","fk750p","fk708","fk20388","fk753","fk20367","fk20376","fk706","fk20386","fk20378","fk20368","fk42229fj","fk20370","fk20358","fk20356","fk10368","fk10355","fk10366","fk14000","fk20357","fhk42307fj","fk10350","fk20366","fk20350","nyk43065","fk10388","fk10367","fk10370","fk20355","fk10386","ff90035c","fhk41307fj","fk12000","nny20378le1","ff90032c"]



    for target in targets:
        r=api.items_search({"manageNumber": target})
        for obj in r["results"]:
            item = obj["item"]
            if not(RakutenMaidoItem.objects.filter(manageNumber= item["manageNumber"]).exists()):
                RakutenMaidoItem.objects.create(manageNumber= item["manageNumber"], updated_at = item["updated"])
            args_updated = dict(updated_at = item["updated"])

            if "title" in item: args_updated["title"] = item["title"]
            if "hideItem" in item: 
                if item["hideItem"] == True:
                    args_updated["hideItem"] = "1"
                else:
                    args_updated["hideItem"] = "0"
            if "features" in item:
                if "searchVisibility" in item["features"]: args_updated["features_searchVisibility"] = item["features"]["searchVisibility"]
                if "shopContact" in item["features"]: args_updated["features_shopContact"] = item["features"]["shopContact"]
                if "displayNormalCartButton" in item["features"]: args_updated["features_displayNormalCartButton"] = item["features"]["displayNormalCartButton"]
                if "inventoryDisplay" in item["features"]: args_updated["features_inventoryDisplay"] = item["features"]["inventoryDisplay"]
            if "payment" in item:
                if "taxIncluded" in item["payment"]: args_updated["payment_taxIncluded"] = item["payment"]["taxIncluded"]
                if "cashOnDeliveryFeeIncluded" in item["payment"]: args_updated["payment_cashOnDeliveryFeeIncluded"] = item["payment"]["cashOnDeliveryFeeIncluded"]

            RakutenMaidoItem.objects.filter(manageNumber= item["manageNumber"]).update(**args_updated)

            skus = item["variants"]
            #SKU
            for sku, detail in skus.items():
                if not(RakutenMaidoSku.objects.filter(skuNumber=sku).exists()):
                    RakutenMaidoSku.objects.create(skuNumber=sku, item= RakutenMaidoItem.objects.get(manageNumber=item["manageNumber"]))

                sku_args_updated = dict()

                if "normalDeliveryDateId" in detail: sku_args_updated["normalDeliveryDateId"] = detail["normalDeliveryDateId"]
                if "standardPrice" in detail: sku_args_updated["standardPrice"] = detail["standardPrice"]
                if "referencePrice" in detail:
                    if "displayType" in detail["referencePrice"]:
                        sku_args_updated["referencePrice_displayType"] = detail["referencePrice"]["displayType"]
                        if detail["referencePrice"]["displayType"] == "OPEN_PRICE":
                            sku_args_updated["referencePrice_value"] = "open"
                        elif detail["referencePrice"]["displayType"] == "SHOP_SETTING":
                            if "value" in detail["referencePrice"]:
                                sku_args_updated["referencePrice_value"] = detail["referencePrice"]["value"]
                if "hidden" in detail: 
                    if detail["hidden"] == True:
                        sku_args_updated["hidden"] = 1
                    else:
                        sku_args_updated["hidden"] = 0
                if "shipping" in detail:
                    if "shippingMethodGroup" in detail["shipping"]: sku_args_updated["shipping_shippingMethodGroup"] = detail["shipping"]["shippingMethodGroup"]
                    if "postageIncluded" in detail["shipping"]: 
                        if detail["shipping"]["postageIncluded"] == True:
                            sku_args_updated["shipping_postageIncluded"] = "1"
                        else:
                            sku_args_updated["shipping_postageIncluded"] = "0"
                RakutenMaidoSku.objects.filter(skuNumber=sku).update(**sku_args_updated)
