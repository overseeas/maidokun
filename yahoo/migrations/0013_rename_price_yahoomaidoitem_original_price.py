# Generated by Django 4.2.16 on 2025-03-17 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yahoo', '0012_remove_yahoocoordiroomitem_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yahoomaidoitem',
            old_name='price',
            new_name='original_price',
        ),
    ]
