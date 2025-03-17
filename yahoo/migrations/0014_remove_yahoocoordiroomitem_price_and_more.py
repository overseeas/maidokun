# Generated by Django 4.2.16 on 2025-03-17 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yahoo', '0013_rename_price_yahoomaidoitem_original_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yahoocoordiroomitem',
            name='price',
        ),
        migrations.AddField(
            model_name='yahoocoordiroomitem',
            name='original_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='yahoomaidoitem',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yahoomaidoitem',
            name='original_price',
            field=models.IntegerField(blank=True),
        ),
    ]
