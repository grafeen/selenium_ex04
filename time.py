import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('incognito')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(url='https://www.google.com/')

time.sleep(1) # 1초 기다림
time.sleep(5.5) # 5.5초 기다림
time.sleep(10) # 10초 기다림

driver.quit()

