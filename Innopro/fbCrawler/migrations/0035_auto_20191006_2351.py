# Generated by Django 2.0.6 on 2019-10-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbCrawler', '0034_auto_20191002_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='vip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=100)),
                ('VIPfbuid', models.CharField(max_length=100)),
                ('VIPusername', models.CharField(max_length=100)),
                ('VIPorder', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='settlementrule',
            name='stockNumFalse',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]