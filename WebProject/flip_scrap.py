
from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located

import pandas as pd
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#options = Options()
#options.headless = True

#driver = webdriver.Chrome(options=options)
#driver.get("https://www.amazon.in")


driver=webdriver.Chrome()
driver.get("https://www.amazon.in")
#element=driver.find_element(By.XPATH,("//*[@id='searchDropdownBox']/option[11]"))
# find id of option
x = driver.find_element(By.ID,'searchDropdownBox')
drop = Select(x)
drop.select_by_visible_text("Books")
driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]').click()
#driver.find_element(By.XPATH,('//*[@id="sobe_d_b_1_7"]')).click()
drop2=driver.find_element(By.XPATH,'//*[@id="nav-subnav"]/a[6]')
# Create an Actions object
actions = ActionChains(driver)
# Move the cursor to the dropdown menu
actions.move_to_element(drop2).perform()
# Click on the dropdown menu
# (This will not actually select an option, just open the menu)
#actions.click(drop2).perform()
#driver.find_element(By.ID,'nav-subnav').click()
 #Wait for the dynamic options to be visible

#options_locator = (By.XPATH, '//*[@id="nav-flyout-ab:books-subnav-flyout-content-3,books-subnav-flyout-promo-3:generic-subnav-flyout"]/div[2]/div/div/ul')

#options = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(options_locator))
#options = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(options_locator))
driver.find_element(By.LINK_TEXT,'Teen & Young Adult').click()
driver.find_element(By.CSS_SELECTOR,'#s-refinements > div:nth-child(12) > ul > li:nth-child(4) > span > a').click()
#'//*[@id="nav-flyout-ab:books-subnav-flyout-content-3,books-subnav-flyout-promo-3:generic-subnav-flyout"]/div[2]/div/div/ul/li[5]'

driver.quit()
