from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
load_dotenv()
import os
import time

url = "https://www.instagram.com/accounts/login/"
SIMILAR_ACCOUNT = "any_instagram_username"
USER = os.getenv("first") + os.getenv("second")  # normally wasn't working so i split the username in two halves
PASS = os.getenv("PASSWORD")
CHROME_DRIVER_PATH = "C://Development//chromedriver.exe"


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.followers_list = None

    def login(self):
        self.driver.get(url)
        time.sleep(2)
        u_name = self.driver.find_element_by_name('username')
        u_pass = self.driver.find_element_by_name("password")
        u_name.send_keys(USER)
        u_pass.send_keys(PASS)
        time.sleep(2)
        u_pass.send_keys(Keys.ENTER)

    def find_followers(self):
        new_url = "https://www.instagram.com/" + SIMILAR_ACCOUNT
        self.driver.get(new_url)
        time.sleep(2)
        followers = self.driver.find_element_by_xpath(
            "//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a")
        followers.click()
        time.sleep(2)
        self.followers_list = self.driver.find_elements_by_css_selector("li button")

    def follow(self):
        count = 0
        for people in self.followers_list:
            while count < 2:
                people.click()
                count += 1


insta_bot = InstaFollower()
insta_bot.login()
time.sleep(3)
insta_bot.find_followers()
insta_bot.follow()
