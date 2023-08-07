from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
dropdown = driver.find_element(By.ID, 'searchDropdownBox')
select = Select(dropdown)
select.select_by_value('search-alias=stripbooks')  # Replace with the value of the desired option
driver.find_element(By.ID, 'nav-search-submit-button').click()
driver.find_element((By.XPATH,'//*[@id="contentGrid_525626"]/div/div[2]/div[2]/div/div/a')).click()


driver.close()
