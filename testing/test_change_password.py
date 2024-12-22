# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# EMAIL = 'helal@gmail.com'
# PASSWORD = '000000'
# NEW_PASSWORD = '999999'

# service = Service('chromedriver.exe')  
# driver = webdriver.Chrome(service=service)  

# wait = WebDriverWait(driver, 50)  

# try:
#     driver.get('http://127.0.0.1:5000/login')
#     print("Navigated to login page.")

#     # Log in
#     email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
#     email_input.send_keys(EMAIL)
#     print("Email entered.")

#     password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
#     password_input.send_keys(PASSWORD)
#     print("Password entered.")

#     login_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
#     login_button.click()
#     print("Clicked login button.")

#     wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'container')))
#     print("Login successful.")

#     # Navigate to Change Password page
#     account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Account")))
#     account_link.click()
#     print("Navigated to Account page.")

#     profile_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Profile")))
#     profile_link.click()
#     print("Navigated to Profile page.")

#     change_password_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Change Password")))
#     change_password_link.click()
#     print("Navigated to Change Password page.")

#     # Wait for form to load
#     wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'container')))
#     print("Change Password form loaded.")

#     # Fill in the form
#     current_password_input = wait.until(EC.presence_of_element_located((By.ID, "current_password")))
#     current_password_input.send_keys(PASSWORD)
#     print("Current password entered.")

#     new_password_input = wait.until(EC.presence_of_element_located((By.ID, "new_password")))
#     new_password_input.send_keys(NEW_PASSWORD)
#     print("New password entered.")

#     confirm_new_password_input = wait.until(EC.presence_of_element_located((By.ID, "confirm_new_password")))
#     confirm_new_password_input.send_keys(NEW_PASSWORD)
#     print("Confirmed new password.")

#     # Submit the form
#     change_password_button = wait.until(EC.element_to_be_clickable((By.ID, "change_password")))
#     change_password_button.click()
#     print("Clicked Change Password button.")

#     # Check for success
#     success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "success")))
#     print("Password change successful:", success_message.text)

#     # Take a screenshot
#     driver.save_screenshot('change_password_success.png')
#     print("Screenshot saved.")

# except Exception as e:
#     print("An error occurred:", e)
#     driver.save_screenshot('error_screenshot.png')  # Save screenshot for debugging

# finally:
#     driver.quit()



         
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = 'helal@gmail.com'
PASSWORD = '000000'
NEW_PASSWORD = '999999'

# Automatically download and set up chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 5)

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

    # Navigate to Change Password page
    account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Account")))
    account_link.click()
    print("Navigated to Account page.")

    profile_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Profile")))
    profile_link.click()
    print("Navigated to Profile page.")

    change_password_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Change Password")))
    change_password_link.click()
    print("Navigated to Change Password page.")

    # Wait for form to load
    print("Change Password form loaded.")

    # Fill in the form
    # Wait for the current password field and fill it with the PASSWORD variable
    current_password_input = wait.until(EC.presence_of_element_located((By.ID, "current_password")))
    current_password_input.clear()  # Clear any existing value in the field
    current_password_input.send_keys(PASSWORD)  # Type the current password into the field
    print("Current password entered.")

    # Wait for the new password field and fill it with the NEW_PASSWORD variable
    new_password_input = wait.until(EC.presence_of_element_located((By.ID, "new_password")))
    new_password_input.clear()  # Clear any existing value in the field
    new_password_input.send_keys(NEW_PASSWORD)  # Type the new password into the field
    print("New password entered.")

    # Wait for the confirm new password field and fill it with the NEW_PASSWORD variable
    confirm_new_password_input = wait.until(EC.presence_of_element_located((By.ID, "confirm_new_password")))
    confirm_new_password_input.clear()  # Clear any existing value in the field
    confirm_new_password_input.send_keys(NEW_PASSWORD)  # Confirm the new password into the field
    print("Confirmed new password.")

    # Wait for and click the Change Password button
    change_password_button = wait.until(EC.element_to_be_clickable((By.ID, "change_password")))
    change_password_button.click()
    print("Clicked Change Password button.")

    # Check for success message
    success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "success")))
    print("Password change successful:", success_message.text)


    # Take a screenshot
    driver.save_screenshot('change_password_success.png')
    print("Screenshot saved.")

except Exception as e:
    print("An error occurred:", e)
    driver.save_screenshot('error_screenshot.png')  # Save screenshot for debugging


driver.quit()