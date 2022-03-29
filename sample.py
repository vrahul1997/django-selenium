# import subprocess

# commands = ['make worker', 'make server', 'make beatDB']
# procs = [subprocess.Popen(i, shell=True) for i in commands]
# for p in procs:
#     p.wait()


import time
from selenium import webdriver

driver = webdriver.Remote()

driver.get("https://tv.bell.ca/login")
time.sleep(10)
driver.get_screenshot_as_file("sample_screenshot.png")
driver.close()
