from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define your credentials
EMAIL = 'helal@gmail.com'
PASSWORD = '000000'

# Use webdriver-manager to automatically install and set up chromedriver for Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 10)  # 10 seconds timeout

try:
    # Log in with the provided credentials
    driver.get('http://127.0.0.1:5000/login')
    print("Navigated to login page.")

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

    # Navigate to the homepage
    driver.get('http://127.0.0.1:5000/')
    print("Navigated to homepage.")

    cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Cart")))
    cart_link.click()
    print("Navigated to account page.")

    # Wait for the account page to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'container')))
    print("Account page loaded.")

    print("Logout successful.")
    # Take a screenshot after logout
    driver.save_screenshot('logged_out.png')
    print("Logged out screenshot saved.")
    

except Exception as e:
    print("An error occurred:", e)
    driver.save_screenshot('error_screenshot.png')
    print("Error screenshot saved as 'error_screenshot.png'.")

finally:
    # Close the browser after testing
    driver.quit()
