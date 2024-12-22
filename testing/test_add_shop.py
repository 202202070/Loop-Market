import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  
EMAIL = 'admin@gmail.com'
PASSWORD = '111111'

service = Service(ChromeDriverManager().install())  
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 5)

try:
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

    driver.get('http://127.0.0.1:5000/admin-page')
    print("Navigated to Admin page.")

   
    print("Admin page loaded.")

    time.sleep(1)  

    current_url = driver.current_url
    print(f"Current URL: {current_url}")
    expected_url = 'http://127.0.0.1:5000/admin-page'
    print(f"Expected URL: {expected_url}")
    if current_url == expected_url:
        driver.save_screenshot('admin_page_screenshot.png')
        print("Screenshot saved as 'admin_page_screenshot.png'.")
    else:
        print("Not on the admin page, no screenshot taken.")

    AddShopItem_link = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr/td[3]/a')))
    AddShopItem_link.click()
   


    time.sleep(1)  

    current_url = driver.current_url
    print(f"Current URL: {current_url}")
    expected_url = 'http://127.0.0.1:5000/add-shop-items'
    print(f"Expected URL: {expected_url}")
    if current_url == expected_url:
        driver.save_screenshot('addShopItems_screenshot.png')
        print("Screenshot saved as 'addShopItems_screenshot.png'.")
    else:
        print("Not on the Add Shop Items page, no screenshot taken.")

except Exception as e:
    print("An error occurred:", e)
    driver.save_screenshot('error_screenshot.png')
    print("Error screenshot saved as 'error_screenshot.png'.")


driver.quit()
