# Generated by Django 4.2.16 on 2025-03-10 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yahoo', '0004_alter_item_created_at_alter_item_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoordiroomItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField()),
                ('name', models.CharField()),
                ('code', models.CharField()),
                ('sub_code', models.CharField(blank=True)),
                ('original_price', models.DecimalField(blank=True, decimal_places=0, max_digits=10)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=0, max_digits=10)),
                ('options', models.TextField(blank=True)),
                ('ship_weight', models.DecimalField(blank=True, decimal_places=0, max_digits=10)),
                ('display', models.BooleanField(default=False)),
                ('delivery', models.CharField(blank=True)),
                ('product_category', models.CharField()),
                ('spec1', models.CharField(blank=True)),
                ('spec2', models.CharField(blank=True)),
                ('spec3', models.CharField(blank=True)),
                ('spec4', models.CharField(blank=True)),
                ('spec5', models.CharField(blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Item',
            new_name='MaidoItem',
        ),
    ]
