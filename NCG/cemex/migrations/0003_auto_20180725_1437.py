# Generated by Django 2.0.3 on 2018-07-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemex', '0002_auto_20180721_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
