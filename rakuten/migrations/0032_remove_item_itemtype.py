# Generated by Django 4.2.16 on 2025-03-24 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rakuten', '0031_remove_item_created_remove_item_features_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='itemType',
        ),
    ]
