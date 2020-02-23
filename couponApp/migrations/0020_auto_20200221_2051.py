# Generated by Django 3.0.2 on 2020-02-22 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('couponApp', '0019_auto_20200221_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='purchasedBy',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='couponApp.User'),
        ),
    ]