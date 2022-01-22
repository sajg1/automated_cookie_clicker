from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# chromedriver must be up to date with latest chrome browser version
chrome_driver_path = '/Users/admin/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Clickable cookie
cookie = driver.find_element(By.XPATH, "//*[@id='cookie']")
# Cookie counter
cookie_tally = driver.find_element(By.XPATH, '//*[@id="money"]')
# Upgrade ID's
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]


start_time = time.time()
timeout_time = start_time + 10

while True:

    cookie.click()

    if time.time() > timeout_time:
        # find web elements for upgrades
        store = driver.find_elements(By.CSS_SELECTOR, '#store b')
        prices = []
        # get prices for upgrades
        for item in store:
            text = item.text
            if text != "":
                price = int(text.split("-")[1].strip().replace(",",""))
            prices.append(price)

        # create dictionary with prices and upgrade_id
        upgrades_dict = {}
        for n in range(1, len(prices)):
            upgrades_dict[prices[n]] = item_ids[n]

        cookie_tally = driver.find_element(By.CSS_SELECTOR, 'div #money').text

        if "," in cookie_tally:
            cookie_tally = cookie_tally.replace(",", "")

        # dictionary of upgrades that can be purchased
        affordable_upgrades = {}
        for cost, id in upgrades_dict.items():
            if int(cookie_tally) > cost:
                affordable_upgrades[cost] = id
        print(affordable_upgrades)

        # highest priced upgrade that can be purchased
        if len(affordable_upgrades) > 0:
            highest_upgrade = max(affordable_upgrades)

            # click the highest possible upgrade
            driver.find_element(By.ID, upgrades_dict[highest_upgrade]).click()
        # add 5 seconds
        timeout_time += 10

        # break out of loop after 5 minutes
        if time.time() > start_time + 60 * 5:
            print(driver.find_element(By.CSS_SELECTOR, "div #cps").text.split(":")[1].strip())
            break










