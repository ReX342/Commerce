# Generated by Django 3.2.9 on 2021-12-06 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20211206_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listings',
            name='category',
            field=models.CharField(choices=[('LAP', 'Laptop'), ('CON', 'Console'), ('GAD', 'Gadget'), ('GAM', 'Game'), ('TEL', 'TV'), ('FAS', 'Fashion'), ('TOY', 'Toys'), ('ELE', 'Electronics'), ('HOM', 'Home')], max_length=45),
        ),
    ]
