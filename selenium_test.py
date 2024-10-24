from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Set up Webdriver using WebDriver Manager to automatically manage ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

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
