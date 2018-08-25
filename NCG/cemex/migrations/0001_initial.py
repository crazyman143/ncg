# Generated by Django 2.0.3 on 2018-07-17 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=250)),
                ('image', models.FileField(blank=True, upload_to='item_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cemex.Attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('complete', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cemex.Item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cemex.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Item_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cemex.Attribute')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cemex.Option')),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cemex.Order_Item')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cemex.Item'),
        ),
    ]
