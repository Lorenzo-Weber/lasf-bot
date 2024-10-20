from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

CHROME_DRIVER_PATH = '/usr/local/bin/chromedriver'
USER_DATA_DIR = os.path.expanduser('~/whatsapp_profile')

log_file_path = os.path.join('/home/lorenzo/workspace/python/lasf-bot/log.txt')

def send_file(group_name):
    try:
        service = Service(executable_path=CHROME_DRIVER_PATH)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"user-data-dir={USER_DATA_DIR}")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')  

        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get('https://web.whatsapp.com')

        wait = WebDriverWait(driver, 60)  

        search_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
        search_box.click()
        search_box.send_keys(group_name)
        time.sleep(3)

        try:
            group_title = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[@title="{group_name}"]')))
            group_title.click()
        except Exception as e:
            print(f"Erro ao encontrar o grupo: {group_name} {e}")
            driver.quit()
            return False

        time.sleep(3)

        attach_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="plus"]')))
        attach_button.click()

        file_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))

        if os.path.exists(log_file_path):
            print(f"File exists: {log_file_path}")
            file_input.send_keys(log_file_path)
        else:
            print(f"File not found: {log_file_path}")
            driver.quit()
            return False

        time.sleep(3)

        send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]')))
        send_button.click()

        time.sleep(5)

    except Exception as e:
        print(f"Erro: {e}")
    
    finally:
        driver.quit()
        return True
