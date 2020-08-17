# Remember to run:
# pip install webdriver-manager selenium
# before starting Jupyter

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

import time
driver = webdriver.Chrome(ChromeDriverManager().install())

def login():
    url      = "https://www.campbells.com.au/convenience/"
    username = '0032353419'
    password = 'Australia@1'
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
    time.sleep(1)
    driver.find_element_by_class_name("loginLink").click()
    time.sleep(1)
    driver.find_element_by_id("j_username").send_keys(username)
    time.sleep(1)
    driver.find_element_by_id("j_password").send_keys(password)
    time.sleep(1)
    driver.find_element_by_id('loginButton').click()
    
login()
