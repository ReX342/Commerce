# Generated by Django 3.2.9 on 2021-12-11 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20211210_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments_al',
            name='user',
        ),
        migrations.AddField(
            model_name='comments_al',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]