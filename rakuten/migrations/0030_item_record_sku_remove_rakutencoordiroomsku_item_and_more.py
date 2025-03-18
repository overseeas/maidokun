# Generated by Django 4.2.16 on 2025-03-18 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0013_remove_item_bargain_price_remove_item_jan_code_and_more'),
        ('rakuten', '0029_alter_rakutencoordiroomitem_itemtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manageNumber', models.CharField()),
                ('title', models.CharField()),
                ('itemType', models.CharField(choices=[('NORMAL', '通常商品'), ('PRE_ORDER', '予約商品'), ('SUBSCRIPTION', '定期購入商品')])),
                ('genreId', models.CharField()),
                ('hideItem', models.BooleanField()),
                ('unlimitedInventoryFlag', models.BooleanField()),
                ('features', models.JSONField(default={'displayManufacturerContents': 'メーカー提供情報表示', 'displayNormalCartButton': '注文ボタン', 'displaySubscriptionCartButton': '定期購入ボタン', 'inventoryDisplay': '在庫数表示', 'lowStockThreshold': '残り在庫数表示閾値', 'review': 'レビュー本文表示', 'searchVisiblity': 'サーチ表示', 'shopContact': '商品問い合わせボタン'})),
                ('payment', models.JSONField(default={'cashOnDeliveryFeeIncluded': '代引料', 'taxIncluded': '消費税込み', 'taxRate': '消費税税率'})),
                ('itemDisplaySequence', models.IntegerField()),
                ('layout', models.JSONField(default={'itemLayoutId': '商品ページレイアウト', 'largeDescriptionId': '共通説明文(大)テンプレートID', 'layoutSequenceId': '表示項目の並び順テンプレートID', 'navigationId': 'ヘッダー・フッター・レフトナビのテンプレートID', 'showcaseId': '目玉商品テンプレートID', 'smallDescriptionId': '共通説明文(小)テンプレートID'})),
                ('created', models.DateField()),
                ('updated', models.DateField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='item.item')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField()),
                ('price', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rakuten.item')),
            ],
        ),
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variantId', models.CharField(blank=True, db_index=True, max_length=255)),
                ('referencePrice', models.JSONField(default={'displayType': '表示価格種別', 'type': '表示価格文言', 'value': '表示価格'})),
                ('standardPrice', models.IntegerField(blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rakuten.item')),
            ],
        ),
        migrations.RemoveField(
            model_name='rakutencoordiroomsku',
            name='item',
        ),
        migrations.RemoveField(
            model_name='rakutenmaidoitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='rakutenmaidosku',
            name='item',
        ),
        migrations.DeleteModel(
            name='RakutenCoordiroomItem',
        ),
        migrations.DeleteModel(
            name='RakutenCoordiroomSku',
        ),
        migrations.DeleteModel(
            name='RakutenMaidoItem',
        ),
        migrations.DeleteModel(
            name='RakutenMaidoSku',
        ),
    ]
