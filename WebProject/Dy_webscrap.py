import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import mysql.connector
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/gp/bestsellers/watches/ref=zg_bs_watches_sm")

# Wait for the page to load completely
time.sleep(5)

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
        price=lines[3].strip("₹")
        watch_details.append({'Rank': rank, 'Title': title, 'Sales Info': sales_info,'price':price})
df=[]
df=pd.DataFrame(watch_details)

"""
# Print the watch details
for watch in watch_details:
    print(f"Rank: {watch['Rank']}")
    print(f"Title: {watch['Title']}")
    print(f"Votes: {watch['Sales Info']}")
    print(f"Price : {watch['price']}")
"""
output_file = 'watch_details.xlsx'
df.to_excel(output_file, index=False)

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Prajith@1984',
    database='nba'
)



driver.close()
