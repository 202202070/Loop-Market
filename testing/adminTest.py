import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  # Import webdriver-manager

EMAIL = 'admin@gmail.com'
PASSWORD = '111111'

# Use WebDriver Manager to automatically handle chromedriver
service = Service(ChromeDriverManager().install())  # This will download and install chromedriver
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 50)

try:
    driver.get('http://127.0.0.1:5000/login')
    print("Navigated to login page.")

    # Log in
    email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
    email_input.send_keys(EMAIL)
    print("Email entered.")

    password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys(PASSWORD)
    print("Password entered.")

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
    login_button.click()
    print("Clicked login button.")

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'container')))
    print("Login successful.")

    # Navigate to Admin page
    driver.get('http://127.0.0.1:5000/admin-page')
    print("Navigated to Admin page.")

    # Wait for the admin page to load
    print("Admin page loaded.")

    # Wait for a few seconds before taking the screenshot
    time.sleep(1)  # Wait for 5 seconds

    current_url = driver.current_url
    print(f"Current URL: {current_url}")
    expected_url = 'http://127.0.0.1:5000/admin-page'
    print(f"Expected URL: {expected_url}")
    if current_url == expected_url:
        # Take a screenshot
        driver.save_screenshot('admin_page_screenshot.png')
        print("Screenshot saved.")
    else:
        print("Not on the admin page, no screenshot taken.")

except Exception as e:
    print("An error occurred:", e)
    driver.save_screenshot('error_screenshot.png')  # Save screenshot for debugging
    print("Error screenshot saved as 'error_screenshot.png'.")

finally:
    driver.quit()
