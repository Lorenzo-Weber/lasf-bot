from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Path to your ChromeDriver (ensure this is the correct path)
CHROME_DRIVER_PATH = '/usr/local/bin/chromedriver'

# Path to the user data directory for Chrome
USER_DATA_DIR = os.path.expanduser('~/whatsapp_profile')  # Change to your desired path

def send(group_name, message):

    service = Service(executable_path=CHROME_DRIVER_PATH)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"user-data-dir={USER_DATA_DIR}")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://web.whatsapp.com')

    wait = WebDriverWait(driver, 60)  # Aumenta o tempo para 60 segundos

    # Aguarda até que a caixa de pesquisa esteja clicável
    search_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
    search_box.click()
    search_box.send_keys(group_name)
    time.sleep(3)

    # Aguarda até que o título do grupo esteja clicável
    try:
        group_title = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[@title="{group_name}"]')))
        group_title.click()
    except Exception as e:
        print(f"Erro ao encontrar o grupo: {group_name} {e}")
        driver.quit()
        return False

    time.sleep(3)

    input_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')))
    input_box.click()
    input_box.send_keys(message)
    input_box.send_keys(Keys.ENTER)  

    time.sleep(5)
    return True
    driver.quit()

