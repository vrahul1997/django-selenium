# Generated by Django 3.0.7 on 2022-02-28 11:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vod_testing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fonsevodasset',
            name='asset_found',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fonsevodasset',
            name='asset_pass_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fonsevodasset',
            name='asset_play_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fonsevodasset',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fonsevodasset',
            name='error_screenshot',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='fonsevodasset',
            name='overall_status',
            field=models.CharField(default='#', max_length=200),
        ),
        migrations.AddField(
            model_name='fonsevodasset',
            name='test_end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fonsevodasset',
            name='test_start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]