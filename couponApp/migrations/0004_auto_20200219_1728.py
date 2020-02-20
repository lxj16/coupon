# Generated by Django 3.0.2 on 2020-02-20 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couponApp', '0003_brand_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='brand',
        ),
        migrations.AddField(
            model_name='coupon',
            name='brand',
            field=models.ManyToManyField(to='couponApp.Brand'),
        ),
    ]
