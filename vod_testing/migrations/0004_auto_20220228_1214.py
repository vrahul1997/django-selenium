# Generated by Django 3.0.7 on 2022-02-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vod_testing', '0003_auto_20220228_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fonsevodasset',
            name='error_screenshot',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]