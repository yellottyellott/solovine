# Generated by Django 2.1 on 2018-09-14 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_comment_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.URLField(null=True),
        ),
    ]
