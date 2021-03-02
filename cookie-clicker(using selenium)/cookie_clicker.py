from selenium import webdriver
import time

chrome_driver_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")
items = driver.find_elements_by_css_selector("#store div")
items_id = [item.get_attribute("id") for item in items]
pause = time.time() + 1
tot_time = time.time() + 5*60

while True:
    cookie.click()

    if time.time() > pause:
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        for price in all_prices:
            text = price.text
            if text != "":
                cost = int(text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = items_id[n]

        money = driver.find_element_by_id("money").text
        if "," in money:
            money = money.replace(",", "")

        tot_cookies = int(money)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if tot_cookies > cost:
                affordable_upgrades[cost] = id

        highest_upgrade = max(affordable_upgrades)
        # print(highest_upgrade)
        purchase_id = affordable_upgrades[highest_upgrade]
        purchasing_item = driver.find_element_by_id(purchase_id)
        purchasing_item.click()

        pause = time.time() + 1

    if time.time() > tot_time:
        final_speed = driver.find_element_by_id("cps").text
        print("Final cookie clicking speed: ", final_speed)
        break

driver.quit()
