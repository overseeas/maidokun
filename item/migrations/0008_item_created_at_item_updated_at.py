# Generated by Django 4.2.16 on 2025-03-04 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_delete_category_item_category_item_classification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
