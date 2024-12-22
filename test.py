from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = 'admin@gmail.com'
PASSWORD = '111111'

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
  
    driver.save_screenshot('login_screenshot1.png')  

    print("Page title after login:", driver.title)

except Exception as e:
    print("An error occurred:", e)
    driver.save_screenshot('error login.png')  # Save screenshot for debugging
    print("Error screenshot saved as 'error login.png'.")

driver.quit()
