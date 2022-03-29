import pandas as pd
from driver import driver_constants
from .models import FonseVODAsset

column_names = ['provider_id', 'provider_name', 'title', 'media_name',
                'season_number', 'episode_number', 'sort_title', 'title_brief', 'title_medium', 'series_stacked']


def parse_csv(path):
    dataframe = pd.read_csv(
        path, sep='|', encoding="latin-1")
    dataframe.columns = column_names
    dataframe = dataframe.drop(['series_stacked'], axis=1)
    return dataframe


def import_asset():
    df = parse_csv(driver_constants.ASSET_PATH)
    FonseVODAsset.objects.all().delete()
    for _, row in df.iterrows():
        FonseVODAsset.objects.get_or_create(
            provider_id=row['provider_id'],
            provider_name=row['provider_name'],
            title=row['title'],
            media_name=row['media_name'],
            season_number=row['season_number'],
            episode_number=row['episode_number'],
            sort_title=row['sort_title'],
            title_brief=row['title_brief'],
            title_medium=row['title_medium']
        )
    print("Imported Successfully")


# schedule, created = IntervalSchedule.objects.get_or_create(
#     every=10,
#     period=IntervalSchedule.SECONDS
# )
# task = PeriodicTask.objects.create(
#     interval=schedule,
#     name='SendLoveTask',
#     task='vod_testing.tasks.send_love',
#     expires=datetime.utcnow() + timedelta(seconds=60*60*24*30)
# )
# task.save()
