# Generated by Django 3.2.4 on 2021-06-24 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0005_product_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_amount', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.shop')),
            ],
        ),
    ]
