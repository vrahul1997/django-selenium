# import subprocess

# commands = ['make worker', 'make server', 'make beatDB']
# procs = [subprocess.Popen(i, shell=True) for i in commands]
# for p in procs:
#     p.wait()


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pdb

s = Service(ChromeDriverManager().install())
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
print(user_agent)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("window-size=1280,800")
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://tv.bell.ca/login")
time.sleep(10)
driver.get_screenshot_as_file("sample_screenshot.png")
driver.close()
