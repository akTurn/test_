import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

# Instantiate the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/gp/bestsellers/watches/ref=zg_bs_watches_sm")

# Wait for the page to load completely
time.sleep(5)

# Scroll down to the end of the page
body = driver.find_element(By.TAG_NAME, 'body')
body.send_keys(Keys.END)
time.sleep(2)

# Keep scrolling until the end of the page
while True:
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    body.send_keys(Keys.END)
    time.sleep(2)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break

# Scrape the watch details
watch_details = []
element = driver.find_element(By.XPATH, "//*[@id='zg']/div/div")
watchdetails = element.text

# Split the watch details by "#"
sections = watchdetails.split('#')

# Process each section
for section in sections:
    # Split the section by new lines
    lines = section.split('\n')
    # Ignore empty sections or sections with fewer than three lines
    if len(lines) >= 3:
        rank = lines[0]
        title = lines[1]
        sales_info = lines[2]
        watch_details.append({'Rank': rank, 'Title': title, 'Sales Info': sales_info})

# Create a DataFrame from the watch details
df = pd.DataFrame(watch_details)

# Save the DataFrame to an Excel file
output_file = 'watch_details1.xlsx'
df.to_excel(output_file, index=False)

driver.close()
