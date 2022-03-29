from django.utils import timezone
from django.db import models

# Create your models here.


class FonseVODAsset(models.Model):
    provider_id = models.CharField(max_length=100, null=True)
    provider_name = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    media_name = models.CharField(max_length=100, null=True)
    season_number = models.CharField(max_length=30, null=True)
    episode_number = models.CharField(max_length=30, null=True)
    sort_title = models.CharField(max_length=100, null=True)
    title_brief = models.CharField(max_length=100, null=True)
    title_medium = models.CharField(max_length=100, null=True)
    created_dttm = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True, null=True)
    test_start_time = models.DateTimeField(auto_now_add=False, null=True)
    test_end_time = models.DateTimeField(auto_now_add=False, null=True)
    asset_found = models.BooleanField(null=True)
    asset_pass_status = models.BooleanField(null=True)
    asset_play_status = models.BooleanField(null=True)
    overall_status = models.CharField(max_length=200, default="#")
    error_screenshot = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "fonse_vod_assets"
        verbose_name = 'FONSE VOD asset'

    def __str__(self):
        return self.sort_title
