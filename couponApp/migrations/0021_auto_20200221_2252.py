# Generated by Django 3.0.2 on 2020-02-22 06:52

import couponApp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('couponApp', '0020_auto_20200221_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='coupon',
            new_name='coupons',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='item',
            new_name='coupon',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ordered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='expireDate',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='ordered',
        ),
        migrations.RemoveField(
            model_name='promote',
            name='startDate',
        ),
        migrations.AddField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='code',
            field=models.CharField(default=couponApp.models._randomIDGenerator, max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='expireDate',
            field=models.DateTimeField(blank=True, default=couponApp.models._three_month_from_now, null=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='img',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='paymentPercentage',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='coupon',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='couponApp.Brand'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='user',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='estimatePurchaseAmount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='user',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='promote',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
