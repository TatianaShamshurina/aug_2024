# https://magento.softwaretestingboard.com/gear/bags.html
"""
import time
from selenium import webdriver


# Set up the WebDriver (this example uses Chrome)
driver = webdriver.Chrome()

# Open a web page
#driver.get("https://www.example.com")
driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
time.sleep(3)
# Optional: Print the title of the page
print(driver.title)

# Close the browser
driver.quit()
"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#service = Service(ChromeDriverManager(driver_version="126.0.6478.127").install())
service = Service(ChromeDriverManager(driver_version="126.0.6478.127").install())
driver = webdriver.Chrome(service=service)

driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
time.sleep(3)

price = "//span[@class='price']"