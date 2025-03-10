# Generated by Django 4.2.16 on 2025-03-10 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rakuten', '0019_rename_coordiroomitem_rakutencoordiroomitem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='accessControl',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='customizationOptions',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='features',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='images',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='layout',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='payment',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='pointCampaign',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='precautions',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='purchasablePeriod',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='subscription',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='tags',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='updated',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='variantSelectors',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='video',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomitem',
            name='whiteBgImage',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomsku',
            name='articleNumber',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomsku',
            name='articleNumberForSet',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomsku',
            name='attributes',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomsku',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomsku',
            name='features',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomsku',
            name='images',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomsku',
            name='referencePrice',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomsku',
            name='selectorValues',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomsku',
            name='shipping',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomsku',
            name='specs',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomsku',
            name='subscriptionPrice',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutencoordiroomsku',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='accessControl',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='customizationOptions',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='features',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='images',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='layout',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='payment',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='pointCampaign',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='precautions',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='purchasablePeriod',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='subscription',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='tags',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='updated',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='variantSelectors',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='video',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidoitem',
            name='whiteBgImage',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidosku',
            name='articleNumber',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidosku',
            name='articleNumberForSet',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidosku',
            name='attributes',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidosku',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidosku',
            name='features',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidosku',
            name='images',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidosku',
            name='referencePrice',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidosku',
            name='selectorValues',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidosku',
            name='shipping',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidosku',
            name='specs',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidosku',
            name='subscriptionPrice',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='rakutenmaidosku',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
