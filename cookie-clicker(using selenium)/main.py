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
time.sleep(10)
driver.quit()
















# from selenium import webdriver
# import time
#
# chrome_driver_path = YOUR CHROME DRIVER PATH
# driver = webdriver.Chrome(chrome_driver_path)
# driver.get("http://orteil.dashnet.org/experiments/cookie/")
#
# #Get cookie to click on.
# cookie = driver.find_element_by_id("cookie")
#
# #Get upgrade item ids.
# items = driver.find_elements_by_css_selector("#store div")
# item_ids = [item.get_attribute("id") for item in items]
#
# timeout = time.time() + 5
# five_min = time.time() + 60*5 # 5minutes
#
# while True:
#     cookie.click()
#
#     #Every 5 seconds:
#     if time.time() > timeout:
#
#         #Get all upgrade <b> tags
#         all_prices = driver.find_elements_by_css_selector("#store b")
#         item_prices = []
#
#         #Convert <b> text into an integer price.
#         for price in all_prices:
#             element_text = price.text
#             if element_text != "":
#                 cost = int(element_text.split("-")[1].strip().replace(",", ""))
#                 item_prices.append(cost)
#
#         #Create dictionary of store items and prices
#         cookie_upgrades = {}
#         for n in range(len(item_prices)):
#             cookie_upgrades[item_prices[n]] = item_ids[n]
#
#         #Get current cookie count
#         money_element = driver.find_element_by_id("money").text
#         if "," in money_element:
#             money_element = money_element.replace(",", "")
#         cookie_count = int(money_element)
#
#         #Find upgrades that we can currently afford
#         affordable_upgrades = {}
#         for cost, id in cookie_upgrades.items():
#             if cookie_count > cost:
#                  affordable_upgrades[cost] = id
#
#         #Purchase the most expensive affordable upgrade
#         highest_price_affordable_upgrade = max(affordable_upgrades)
#         print(highest_price_affordable_upgrade)
#         to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
#
#         driver.find_element_by_id(to_purchase_id).click()
#
#         #Add another 5 seconds until the next check
#         timeout = time.time() + 5
#
#     #After 5 minutes stop the bot and check the cookies per second count.
#     if time.time() > five_min:
#         cookie_per_s = driver.find_element_by_id("cps").text
#         print(cookie_per_s)
#         break
#
