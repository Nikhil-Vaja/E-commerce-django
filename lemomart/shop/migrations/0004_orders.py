# Generated by Django 5.0.4 on 2024-05-20 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(default='', max_length=70)),
                ('address', models.CharField(default='', max_length=500)),
                ('address2', models.CharField(default='', max_length=500)),
                ('phone', models.CharField(default='', max_length=99)),
                ('city', models.CharField(default='', max_length=99)),
                ('state', models.CharField(default='', max_length=99)),
                ('pincode', models.CharField(default='', max_length=99)),
            ],
        ),
    ]