# Generated by Django 4.2.16 on 2025-03-10 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rakuten', '0024_alter_rakutencoordiroomsku_attributes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='hideItem',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='hideItem',
            field=models.BooleanField(),
        ),
    ]
