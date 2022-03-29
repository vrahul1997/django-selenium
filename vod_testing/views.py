from django.http import HttpResponse
from vod_testing.scrapper import AssetTesting
from vod_testing.vod_utils import import_asset


"""Sample test"""


def test(request, name="vijay"):
    print(name)
    AssetTesting(driver="chrome")
    print("task done")
    return HttpResponse("<h1>VOD testing</h1>")


def asset(request):
    import_asset()
    return HttpResponse("<h1>Imported succesfully</h1>")
