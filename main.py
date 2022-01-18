from selenium import webdriver
import time

# chromedriver must be up to date with latest chrome browser version
chrome_driver_path = '/Users/admin/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Clickable cookie
cookie = driver.find_element_by_xpath("//*[@id='cookie']")
# Cookie counter
cookie_tally = driver.find_element_by_xpath('//*[@id="money"]')
# Clickable store upgrades
cursor_upgrade = driver.find_element_by_xpath('//*[@id="buyCursor"]')
grandma_upgrade = driver.find_element_by_xpath('//*[@id="buyGrandma"]')
factory_upgrade = driver.find_element_by_xpath('//*[@id="buyFactory"]')
mine_upgrade = driver.find_element_by_xpath('//*[@id="buyMine"]')
shipment_upgrade = driver.find_element_by_xpath('//*[@id="buyShipment"]')
alchemy_upgrade = driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]')
portal_upgrade = driver.find_element_by_xpath('//*[@id="buyPortal"]')
time_machine_upgrade = driver.find_element_by_xpath('//*[@id="buyTime machine"]')


store = driver.find_elements_by_class_name('grayed')

cost_cursor = store[0].text.split(' ')[2].split('\n')[0]
print(cost_cursor)


# start_time = time.time()
# check_time = start_time + 5
# running = True
#
# while running:
#     if time.time() > check_time:
#         running = False
#
#     else:
#         cookie.click()
#
# print(cookie_tally.text)





