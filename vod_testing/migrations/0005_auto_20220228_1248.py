# Generated by Django 3.0.7 on 2022-02-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vod_testing', '0004_auto_20220228_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fonsevodasset',
            name='asset_found',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='fonsevodasset',
            name='asset_pass_status',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='fonsevodasset',
            name='asset_play_status',
            field=models.BooleanField(null=True),
        ),
    ]
