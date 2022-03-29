import os
from selenium import webdriver
from mr_vod.settings import BASE_DIR

"""   CREDENTIALS   """
USERNAME = os.getenv("BELL_USERNAME")
PASSWORD = os.getenv("BELL_PASSWORD")
ASSET_PATH = os.getenv("VOD_ASSET_PATH")
ASSET_AVAILABILITY = True

"""   CHROME   """
CHROME_PATH = os.path.join(BASE_DIR, os.getenv("CHROME_DRIVER_PATH"))
CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_argument("--incognito")
# CHROME_OPTIONS.add_argument("--headless")

"""   MOZILLA   """
FIREFOX_PATH = os.path.join(BASE_DIR, os.getenv("FIREFOX_DRIVER_PATH"))
FIREFOX_OPTIONS = webdriver.FirefoxOptions()
FIREFOX_OPTIONS.add_argument("--incognito")


"""   STATUS CONSTANTS   """
STATUS_1 = "Asset not found"
STATUS_2 = "Asset found and not playable"
STATUS_3 = "Asset found and playable"
STATUS_4 = "Asset found but play button is disabled"
STATUS_5 = "Error in Playing content"
