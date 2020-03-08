# Generated by Django 3.0 on 2020-03-06 02:40

import couponApp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('couponApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldCoupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=couponApp.models._randomIDGenerator, max_length=50, unique=True)),
                ('used', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='couponApp.OrderItem')),
            ],
        ),
    ]
