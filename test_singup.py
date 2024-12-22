import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define your credentials
EMAIL = 'al@gmail.com'
USERNAME = 'elal'
PASSWORD = '0000'
CONFIRM_PASSWORD = '0000'

# Initialize Chrome WebDriver (assuming chromedriver.exe is in the current directory or in PATH)
service = Service('chromedriver.exe')  # Ensure chromedriver.exe is in the specified path
driver = webdriver.Chrome(service=service)  # Initialize the Chrome WebDriver

wait = WebDriverWait(driver, 5)  # 50 seconds timeout

try:
    # Navigate to the sign-up page
    driver.get('http://127.0.0.1:5000/sign-up')
    print("Navigated to sign-up page.")

    # Locate and fill the sign-up form
    email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))  # Wait for 'email' to be visible
    email_input.send_keys(EMAIL)
    print("Email entered.")

    username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))  # Wait for 'username' to be visible
    username_input.send_keys(USERNAME)
    print("Username entered.")

    password_input = wait.until(EC.presence_of_element_located((By.ID, "password1")))  # Wait for 'password1' to be visible
    password_input.send_keys(PASSWORD)
    print("Password entered.")

    confirm_password_input = wait.until(EC.presence_of_element_located((By.ID, "password2")))  # Wait for 'password2' to be visible
    confirm_password_input.send_keys(CONFIRM_PASSWORD)
    print("Confirm password entered.")

    # Click the sign-up button
    signup_button = wait.until(EC.element_to_be_clickable((By.ID, "wp-submit")))  # Wait for 'wp-submit' button to be clickable
    signup_button.click()
    print("Clicked sign-up button.")

    # Wait for a few seconds before taking the screenshot
    time.sleep(5)  # Wait for 5 seconds

    # Take a screenshot
    driver.save_screenshot('signup_screenshot1.png')  # Saves screenshot to 'signup_screenshot1.png'
    print("Screenshot saved as 'signup_screenshot1.png'.")

    # Print the title of the page after signup
    print("Page title after signup:", driver.title)

except Exception as e:
    print("An error occurred:", e)
    driver.save_screenshot('singup_error.png')  # Save screenshot for debugging
    print("Error screenshot saved as 'singup_error.png'.")

driver.quit()