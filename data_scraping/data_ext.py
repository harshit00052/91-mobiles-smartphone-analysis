from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup, element
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://www.91mobiles.com/phonefinder.php?rangeMaxVal=300000&filters=rngFl_product_status.price.wap=0-300000.01')
time.sleep(2)

html_code = driver.page_source

height = driver.execute_script('return document.body.scrollHeight')

while True:

    load_more = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="load-more-button"]/span')
        )
    )
    print("button found")
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        load_more
    )
    print("scrolled")
    driver.execute_script(
        "arguments[0].click();",
        load_more
    )
    print("clicked")

    time.sleep(10)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if(height == new_height):
        break
    height = new_height

