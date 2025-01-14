# Generated by Django 2.0.6 on 2019-09-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbCrawler', '0031_auto_20190930_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='ship_method',
            field=models.CharField(blank=True, default='ship', max_length=50, null=True, verbose_name='取貨方式'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='ship_time',
            field=models.CharField(blank=True, default='all', max_length=50, null=True, verbose_name='配送時段'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='transfer_account',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='轉出帳號末五碼'),
        ),
    ]
