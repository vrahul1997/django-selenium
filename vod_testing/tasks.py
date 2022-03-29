import time

from celery import shared_task
from mr_vod.celery import app

from vod_testing.scrapper import AssetTesting


# sharedtask is something you will assign to a heavy task in your business logic
# asynchronous
@shared_task(bind=True)
def send_response(self, name):
    print("===============>  something")
    time.sleep(10)
    print(f"Hello: {name}")
    print("===============>  something")
    return "Done"


@app.task()
def celery_vod_task():
    AssetTesting(driver="chrome")
