from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

'''
This is used to check when the salary data was last updated 
to calculate 2024 salary data later.
'''

# Set up Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL of the page containing the data update info
url = "https://data.louisvilleky.gov/datasets/8bd82421c9b94c37925fb37edaa1c5e8_0/explore"

# Open the URL with Selenium
driver.get(url)

# Give some time for the page to load
driver.implicitly_wait(5)

# Targeting the specific list item that contains the "Data Updated" date and label
data_updated_item = driver.find_element(By.CSS_SELECTOR, "li.metadata-item[data-test='modified']")

# Extract both the date and label text
date_div = data_updated_item.find_elements(By.TAG_NAME, 'div')[0].text
label_div = data_updated_item.find_elements(By.TAG_NAME, 'div')[1].text

# Print the extracted information
print(f"Data Updated Date: {date_div}")
print(f"Label: {label_div}")

# Close the driver
driver.quit()
