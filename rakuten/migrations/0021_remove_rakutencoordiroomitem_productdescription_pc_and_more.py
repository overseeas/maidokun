# Generated by Django 4.2.16 on 2025-03-10 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rakuten', '0020_alter_rakutencoordiroomitem_accesscontrol_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rakutencoordiroomitem',
            name='productDescription_pc',
        ),
        migrations.RemoveField(
            model_name='rakutencoordiroomitem',
            name='productDescription_sp',
        ),
        migrations.RemoveField(
            model_name='rakutenmaidoitem',
            name='productDescription_pc',
        ),
        migrations.RemoveField(
            model_name='rakutenmaidoitem',
            name='productDescription_sp',
        ),
        migrations.AddField(
            model_name='rakutencoordiroomitem',
            name='productDescription',
            field=models.JSONField(default={'pc': None, 'sp': None}),
        ),
        migrations.AddField(
            model_name='rakutenmaidoitem',
            name='productDescription',
            field=models.JSONField(default={'pc': 'PC要商品説明文', 'sp': 'スマートフォン要商品説明文'}),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='hideItem',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='images',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='precautions',
            field=models.JSONField(default={'agreement': None, 'description': None}),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='customizationOptions',
            field=models.JSONField(default={'customizationOptions': [{'displayName': '商品オプション（項目選択肢）項目名', 'inputType': '商品オプション選択肢タイプ', 'required': '商品オプション必須フラグ', 'selections': [{'displayValue': '商品オプション選択肢名'}]}]}),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='images',
            field=models.JSONField(default={'images': [{'alt': '商品画像名（ALT）', 'location': '商品画像種別', 'type': '商品画像種別'}]}),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='precautions',
            field=models.JSONField(default={'agreement': '医療品注意事項', 'description': '医薬品説明文'}),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='tags',
            field=models.JSONField(default={'tags': []}),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='video',
            field=models.JSONField(default={'parameters': {'value': '動画のURL'}, 'type': '動画種別'}),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='whiteBgImage',
            field=models.JSONField(default={'location': '白背景画像URL', 'type': '白背景画像種別'}),
        ),
    ]
