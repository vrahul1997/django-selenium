import platform
import time

from driver import driver_constants
from django.utils import timezone
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from vod_testing.models import FonseVODAsset

from vod_testing.vod_utils import parse_csv


class AssetTesting:

    def __init__(self, driver) -> None:

        if driver == "chrome":
            self.driver = webdriver.Chrome(
                executable_path=driver_constants.CHROME_PATH,
                options=driver_constants.CHROME_OPTIONS
            )

        if driver == "firefox":
            self.driver = webdriver.Firefox(
                executable_path=driver_constants.FIREFOX_PATH,
                options=driver_constants.FIREFOX_OPTIONS
            )

        self.username = driver_constants.USERNAME
        self.password = driver_constants.PASSWORD

        # Initiate the functions
        """Login"""
        try:
            self._login()
        except Exception as e:
            print("Login Failed: ", e)

        """Banner Boxes"""
        try:
            self._clear_banner_boxes()
        except Exception as e:
            print("Welcome Box not found: ", e)

        """find each asset"""
        try:
            self._findAsset()
        except Exception as e:
            print("Asset Error: ", e)

    def _login(self):
        self.driver.get("https://tv.bell.ca/login")
        self.driver.implicitly_wait(5)
        time.sleep(5)
        self.driver.get_screenshot_as_file("screenshot.png")
        best = self.driver.find_element_by_xpath(
            "(.//*[@class='text-title'])[2]")
        best.click()
        self.driver.implicitly_wait(5)

        # username
        username = self.driver.find_element_by_xpath(
            "//input[@placeholder='Username']")
        self.driver.implicitly_wait(5)
        username.click()
        username.send_keys(self.username)
        self.driver.find_element_by_xpath(
            "//div[@class='button-wrapper']/div[text() = 'Next']").click()

        # Password
        password = self.driver.find_element_by_xpath(
            "//input[@placeholder='Password']")
        password.click()
        password.send_keys(self.password)
        self.driver.find_element_by_xpath(
            "//div[@class='button-wrapper']/div[text() = 'Log in']").click()
        print("\n")
        print("===> Login Successful")
        time.sleep(5)

    def _clear_banner_boxes(self):
        self.driver.find_element_by_xpath(
            "//button[@class='shepherd-cancel-icon']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "//button[@class='shepherd-cancel-icon']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "//button[@class='shepherd-cancel-icon']").click()
        print("===> All Banners closed successfully")

    def _findAsset(self):
        asset_set = FonseVODAsset.objects.all().order_by('id')
        for self.db_asset_model in asset_set.iterator():
            self.start_time = timezone.now()
            try:
                search = self.driver.find_element_by_xpath(
                    "//input[@placeholder='Search']")
                search.click()
                search.clear()
                self.driver.implicitly_wait(5)
                print("\n")
                print("Show Name: ", self.db_asset_model.title_medium)
                search.send_keys(self.db_asset_model.title_medium)
                self.driver.implicitly_wait(5)

            except Exception as e:
                print("Search button not found: ", e)
                raise e

            # find the platform
            if platform.system() == "Windows":
                search.send_keys(Keys.ENTER)
                self.driver.implicitly_wait(5)
            else:
                search.send_keys(Keys.RETURN)
                self.driver.implicitly_wait(5)

            # LOOK FOR THE SHOW
            try:
                show = self.driver.find_element_by_xpath(
                    "(//div[@class='cell-primary-image'])[1]")
                show.click()
                driver_constants.ASSET_AVAILABILITY = True
                time.sleep(5)

            except NoSuchElementException as e:
                driver_constants.ASSET_AVAILABILITY = False

            if driver_constants.ASSET_AVAILABILITY == False:
                self.update_fonse_vod_asset(
                    model=self.db_asset_model,
                    found_status=False,
                    pass_status=False,
                    play_status=False,
                    overall=driver_constants.STATUS_1,
                    start_time=self.start_time,
                    end_time=timezone.now()
                )
                print(driver_constants.STATUS_1)

            else:
                try:
                    cancel = self.driver.find_element_by_xpath(
                        "//button[@class='shepherd-cancel-icon']")
                    self.driver.implicitly_wait(5)
                    cancel.click()
                except Exception as e:
                    pass

                # PLAY BUTTON
                try:
                    time.sleep(3)
                    self.play()

                # Unlock content
                except Exception as e:
                    print(".... Checking for Unlock content")
                    try:
                        unlock = self.driver.find_element_by_xpath(
                            "//div[@class='button-ex-label-wrapper' and contains(., 'Unlock')]")
                        if unlock.is_displayed():
                            unlock.click()

                            time.sleep(5)

                            # username
                            username = self.driver.find_element_by_xpath(
                                "//input[@placeholder='Username']")
                            self.driver.implicitly_wait(5)
                            username.click()
                            username.send_keys(self.username)

                            # Password
                            password = self.driver.find_element_by_xpath(
                                "//input[@placeholder='Password']")
                            self.driver.implicitly_wait(5)
                            password.click()
                            password.send_keys(self.password)

                            time.sleep(2)

                            unlock_content = self.driver.find_element_by_xpath(
                                "//div[@class='title-wrapper' and contains(., 'Unlock')]")
                            unlock_content.click()

                            time.sleep(5)
                            # Play content after unlocking it
                            self.play()

                    except Exception as e:
                        print("Error Playing the content")
                        self.update_fonse_vod_asset(
                            model=self.db_asset_model,
                            found_status=True,
                            pass_status=False,
                            play_status=False,
                            overall=driver_constants.STATUS_5,
                            start_time=self.start_time,
                            end_time=timezone.now()
                        )

        self.driver.close()
        print("all done")

    def play(self):
        play = self.driver.find_element_by_xpath(
            "//div[@class='button-ex-label-wrapper' and contains(., 'Play')]")
        if play.is_displayed():
            if play.is_enabled() == True:
                play.click()
                time.sleep(5)

                # PROGRESS BAR
                progress_bar = self.driver.find_element_by_xpath(
                    "//div[@class='progressBar']/div/div/span")
                progress_bar_text = progress_bar.get_attribute(
                    'textContent')

                time.sleep(15)

                progress_bar_after_20 = self.driver.find_element_by_xpath(
                    "//div[@class='progressBar']/div/div/span")
                progress_bar_after_20_text = progress_bar_after_20.get_attribute(
                    'textContent')

                if progress_bar_text != progress_bar_after_20_text:
                    self.update_fonse_vod_asset(
                        model=self.db_asset_model,
                        found_status=True,
                        pass_status=True,
                        play_status=True,
                        overall=driver_constants.STATUS_3,
                        start_time=self.start_time,
                        end_time=timezone.now()
                    )
                    print(driver_constants.STATUS_3)
                    print("\n")

                    # GO BACK TO SEARCH PAGE
                    self.driver.implicitly_wait(5)
                    back = self.driver.find_element_by_xpath(
                        "(//button[contains(@id,'ember')])[1]")
                    back.click()
                    time.sleep(5)
                    show_close = self.driver.find_element_by_xpath(
                        "//button[@class='card-closeButton']")
                    show_close.click()

                else:
                    self.update_fonse_vod_asset(
                        model=self.db_asset_model,
                        found_status=True,
                        pass_status=False,
                        play_status=False,
                        overall=driver_constants.STATUS_2,
                        start_time=self.start_time,
                        end_time=timezone.now()
                    )
                    print(driver_constants.STATUS_2)
                    print("\n")

            else:
                self.update_fonse_vod_asset(
                    model=self.db_asset_model,
                    found_status=True,
                    pass_status=False,
                    play_status=False,
                    overall=driver_constants.STATUS_4,
                    start_time=self.start_time,
                    end_time=timezone.now()
                )
                print(driver_constants.STATUS_4)
                print("\n")
                time.sleep(5)
                show_close = self.driver.find_element_by_xpath(
                    "//button[@class='card-closeButton']")
                show_close.click()

    def update_fonse_vod_asset(self, model: FonseVODAsset, found_status, pass_status, play_status, overall, start_time, end_time):
        model.asset_found = found_status
        model.asset_pass_status = pass_status
        model.asset_play_status = play_status
        model.overall_status = overall
        model.test_start_time = start_time
        model.test_end_time = end_time
        model.save()
