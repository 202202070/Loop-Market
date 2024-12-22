from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = 'dsd@gmail.com'
PASSWORD = '1111'

service = Service('chromedriver.exe')  
driver = webdriver.Chrome(service=service)  

wait = WebDriverWait(driver, 5)  

try:
    driver.get('http://127.0.0.1:5000/login')

    email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))  
    email_input.send_keys(EMAIL)

    password_input = wait.until(EC.presence_of_element_located((By.ID, "password"))) 
    password_input.send_keys(PASSWORD)

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))  
    login_button.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'container')))  

    # Navigate to account page
    account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Account")))
    account_link.click()

    # Navigate to profile page
    profile_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Profile")))
    profile_link.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'container')))  

    driver.save_screenshot('profile_screenshot.png')  
    print("Page title on profile page:", driver.title)

    # Check profile details
    username = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Welcome')]")))
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Email:')]")))

    print("Username on profile page:", username.text)
    print("Email on profile page:", email.text)

except Exception as e:
    print("An error occurred:", e)

    driver.save_screenshot('error profile.png')   
    print("Error screenshot saved as 'error profile.png'.")


driver.quit()