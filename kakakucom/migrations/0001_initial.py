# Generated by Django 4.2.16 on 2025-03-04 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Deliverygroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jan', models.CharField(blank=True)),
                ('code', models.CharField()),
                ('price', models.DecimalField(blank=True, decimal_places=0, max_digits=10)),
                ('delivery', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('store', models.BooleanField(default=False)),
                ('link', models.URLField(blank=True)),
                ('image_url', models.URLField(blank=True)),
                ('comment', models.CharField(blank=True)),
                ('warranty', models.BooleanField(blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='kakakucom.category')),
                ('delivery_group', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='kakakucom.deliverygroup')),
                ('maker', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='kakakucom.maker')),
                ('stock', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='kakakucom.stock')),
            ],
        ),
    ]
