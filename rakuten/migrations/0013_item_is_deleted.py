# Generated by Django 4.2.16 on 2024-12-04 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rakuten', '0012_item_controlcolumn'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_deleted',
            field=models.BooleanField(default=True),
        ),
    ]