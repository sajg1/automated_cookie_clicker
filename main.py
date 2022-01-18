from selenium import webdriver
import time

# chromedriver must be up to date with latest chrome browser version
chrome_driver_path = '/Users/admin/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_xpath("//*[@id='cookie']")
cookie_tally = driver.find_element_by_xpath('//*[@id="money"]')


start_time = time.time()
check_time = start_time + 5
running = True

while running:
    if time.time() > check_time:
        running = False

    else:
        cookie.click()

print(cookie_tally.text)





