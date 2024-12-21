from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define your credentials
EMAIL = 'admin@gmail.com'
PASSWORD = '111111'

# Initialize Chrome WebDriver (assuming chromedriver.exe is in the current directory or in PATH)
service = Service('chromedriver.exe')  # Ensure chromedriver.exe is in the specified path
driver = webdriver.Chrome(service=service)  # Initialize the Chrome WebDriver

# Navigate to the login page
driver.get('http://127.0.0.1:5000/login')

# Wait for the elements to be present on the page
wait = WebDriverWait(driver, 200)  # 10 seconds timeout

# Locate and fill the login form
user_input = wait.until(EC.presence_of_element_located((By.ID, "email")))  # Wait for 'user_login' to be visible
user_input.send_keys(EMAIL)

password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))  # Wait for 'user_pass' to be visible
password_input.send_keys(PASSWORD)

# Click the login button
login_button = wait.until(EC.element_to_be_clickable((By.ID, "wp-submit")))  # Wait for 'wp-submit' button to be clickable
login_button.click()

# Print the title of the page after login
print("Page title after login:", driver.title)

# Close the browser after testing
driver.quit()
