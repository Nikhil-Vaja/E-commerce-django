# Generated by Django 5.0.4 on 2024-05-20 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_orders_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items_json',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
