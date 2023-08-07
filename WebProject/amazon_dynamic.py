from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

# Find the element for "Children's & Young Adult"
young_adult_element = driver.find_element(By.XPATH, "//a[contains(text(),'Children's & Young Adult')]")

# Create an Actions object
actions = ActionChains(driver)

# Move the cursor to the "Children's & Young Adult" element
actions.move_to_element(young_adult_element).perform()

# Wait for the dropdown options to become visible
options_locator = (By.CSS_SELECTOR, '.nav-panel .nav-subcats ul li')
options = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(options_locator))

# Extract the text of the dynamic options
dynamic_options = [option.text.strip() for option in options]

# Print the dynamic options
for option in dynamic_options:
    print(option)

driver.quit()
