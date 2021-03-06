# Generated by Django 3.0.7 on 2022-02-17 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FonseVODAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_id', models.CharField(max_length=100, null=True)),
                ('provider_name', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('media_name', models.CharField(max_length=100, null=True)),
                ('season_number', models.CharField(max_length=30, null=True)),
                ('episode_number', models.CharField(max_length=30, null=True)),
                ('sort_title', models.CharField(max_length=100, null=True)),
                ('title_brief', models.CharField(max_length=100, null=True)),
                ('title_medium', models.CharField(max_length=100, null=True)),
                ('created_dttm', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'FONSE VOD asset',
                'db_table': 'fonse_vod_assets',
            },
        ),
    ]
