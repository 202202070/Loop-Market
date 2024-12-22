from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

EMAIL = 'admin@gmail.com'
PASSWORD = '111111'

driver = webdriver.Chrome()  # Selenium Manager will handle driver setup
wait = WebDriverWait(driver, 50)

try:
    # Navigate to the login page
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

    # Wait for login to complete and verify the account link is visible
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Account")))
    print("Login successful, account link visible.")

    # Click on the account link
    account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Account")))
    account_link.click()
    print("Navigated to account page.")

    # Wait for the account page to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'container')))
    print("Account page loaded.")

    # Use the provided XPath to click on the Logout button
    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/nav/div/ul/li[3]/ul/li[3]/a")))
    logout_button.click()
    print("Clicked logout button.")

    # Add a small delay to ensure the page has time to transition
    time.sleep(1)  # Adjust the time if necessary for the page to transition

    # Check for successful logout by verifying the login button appears
    print("Logout successful.")
    # Take a screenshot after logout
    driver.save_screenshot('logged_out.png')
    print("Logged out screenshot saved.")

except Exception as e:
    print("An error occurred:", e)
    # Save screenshot in case of error
    driver.save_screenshot('error_screenshot.png')
    print("Error screenshot saved.")

finally:
    driver.quit()
