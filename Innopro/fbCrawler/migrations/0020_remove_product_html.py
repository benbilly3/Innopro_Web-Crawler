# Generated by Django 2.0.6 on 2019-09-18 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fbCrawler', '0019_auto_20190911_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='html',
        ),
    ]