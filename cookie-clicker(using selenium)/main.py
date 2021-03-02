from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.youtube.com/")
# sign_in_button = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]")
# print(sign_in_button.text)
# sign_in = driver.find_element_by_link_text("Sign in")
# sign_in.click()
# search_box = driver.find_element_by_name("search_query")
# search_box.send_keys("Anne Marie")
# search_button = driver.find_element_by_id("search-icon-legacy")
# search_button.click()
driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element_by_name("fName")
fname.send_keys("Aakash")
lname = driver.find_element_by_name("lName")
lname.send_keys("Chahal")
email = driver.find_element_by_name("email")
email.send_keys("someone@something.com")
signUp = driver.find_element_by_class_name("btn")
signUp.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()
