# Generated by Django 2.1 on 2018-09-24 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0005_auto_20180924_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssentry',
            name='feed',
            field=models.ForeignKey(blank=True, null=True, on_delete='cascade', to='feeds.RSSFeed'),
        ),
    ]