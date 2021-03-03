from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
load_dotenv()
import time

PROMISED_UP = 50
PROMISED_DOWN = 50
CHROME_DRIVER_PATH = "C://Development//chromedriver.exe"
TWITTER_EMAIL = os.getenv("ACC")
TWITTER_PASS = os.getenv("PASS")


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.down = None
        self.up = None

    def get_internet_speed(self):
        url = "https://www.speedtest.net/"
        self.driver.get(url)
        go = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        time.sleep(60)
        down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = down.text
        up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.up = up.text
        print(float(self.down), self.up)

    def tweet_at_provider(self):
        url = "https://twitter.com/login"
        self.driver.get(url)
        time.sleep(2)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASS)
        password.send_keys(Keys.ENTER)

        time.sleep(2)
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        if int(float(self.up)) < PROMISED_UP and int(float(self.down)) < PROMISED_DOWN:
            tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        else:
            tweet = f"some other tweet if you want..."
        tweet_compose.send_keys(tweet)
        # time.sleep(3)

        # tweet_button = self.driver.find_element_by_xpath(
        #     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        # tweet_button.click()


check = InternetSpeedTwitterBot()
check.get_internet_speed()
check.tweet_at_provider()
