from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up WebDriver
driver = webdriver.Chrome()  # Make sure ChromeDriver is in your PATH

# Open Google
driver.get("https://www.google.com")

# Perform a search
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("QA automation tutorial")
search_box.send_keys(Keys.RETURN)

# Capture and print the title
print(driver.title)

# Close browser
driver.quit()
