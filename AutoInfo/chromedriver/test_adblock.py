import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
from fake_useragent import UserAgent

# useragent = UserAgent()
options = webdriver.ChromeOptions()
# options.add_argument(f"user-agent={useragent.random}")
# options.add_argument('headless')
#set proxy
#options.add_argument("--proxy-server=138.128.91.65:8888")

driver = webdriver.Chrome(
    options=options
    )
url = 'https://google.com/'
driver.get(url=url)
time.sleep(10000)