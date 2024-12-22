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

wait = WebDriverWait(driver, 10)

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

    print("Login successful.")

    # Navigate to Admin page
    driver.get('http://127.0.0.1:5000/customers')

    # Click on the Customers link using the specified XPath
    customers_link = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr/td[1]/a')))
    customers_link.click()
    print("Navigated to Customers page.")
    driver.save_screenshot('customers_screenshot_only.png')
    print("Screenshot saved as 'customers_screenshot_only .png'.")

    # Wait for the customers page to load
    print("Customers page loaded.")

    # Wait for a few seconds before taking the screenshot
    time.sleep(1)  # Wait for 1 second

        
   

except Exception as e:
    print("An error occurred:", e)
    driver.save_screenshot('error_screenshot.png')  # Save screenshot for debugging
    print("Error screenshot saved as 'error_screenshot.png'.")

finally:
    driver.quit()