from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Create ChromeOptions instance
options = Options()

# Initialize WebDriver with Service and Options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# Open Google
driver.get("https://www.google.com")

# Find the search box using its name attribute
search_box = driver.find_element("name", "q")

# Type a search query
search_box.send_keys("Selenium testing in Windows")

# Simulate pressing the Enter key
search_box.send_keys(Keys.RETURN)

# Close the browser
driver.quit()
