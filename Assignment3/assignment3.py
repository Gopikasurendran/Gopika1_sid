# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the timhortons.ca homepage
driver.get("https://www.timhortons.ca/")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","apply") old syntax
apply_button = driver.find_element("xpath","/html/body/reach-portal/div[3]/div/div/div/div/div/div/div[2]/button")
time.sleep(3)

apply_button.send_keys("apply")
time.sleep(3)

# Submitting
apply_button.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(8)
# selecting item
order_now=driver.find_element("xpath","/html/body/div[1]/div/div/div/div/div[2]/div/main/div/div/div/section/div/div/div[2]/div/div/div/div[2]/a/span")
order_now.click()
time.sleep(5)

driver.maximize_window()
time.sleep(3)
#menu
menu_button = driver.find_element("xpath","/html/body/div[1]/div/div/div/div/div[1]/div/nav/div/div[1]/a[2]")
menu_button.click()
time.sleep(5)
# location
search_button = driver.find_element("xpath","/html/body/div[1]/div/div/div/div/div[2]/div/main/div/div/div[2]/div/div[2]/div/div/div/input")
search_button.click()
time.sleep(5)
search_button.send_keys("121 University Avenue East, Waterloo, ON, Canada")
time.sleep(5)
search_button.send_keys(Keys.RETURN)
time.sleep(5)
# search address
location_bar = driver.find_element("xpath","/html/body/div[1]/div/div/div/div/div[2]/div/main/div/div/div[3]/div[2]/div/div[1]/div/div/div/button")
location_bar.click()
time.sleep(8)

# order-now
order_button = driver.find_element("xpath","/html/body/div[1]/div/div/div/div/div[2]/div/main/div/div/div[3]/div[2]/div/div[1]/div[2]/div/div/div[2]/button")
order_button.click()
time.sleep(8)
driver.close()
