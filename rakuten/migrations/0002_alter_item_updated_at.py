# Generated by Django 5.1.1 on 2024-09-30 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rakuten', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
