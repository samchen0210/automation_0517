import logging
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import functions

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read('config.ini')

def run():
    driver = webdriver.Chrome()
    functions.open(driver)

    wait = WebDriverWait(driver, 5)
    accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept All Cookies')]")))
    accept_button.click()

    driver.find_element(By.NAME, 'serial').send_keys(config.get('case_6', 'input_serial'))
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/form/button').click()
    time.sleep(1)

    status = driver.find_element(By.XPATH, '//*[@id="serial"]/following-sibling::div').text
    logging.info('Got information = {}'.format(status))
    functions.write_res(status, 'response', 6)
    
    if status == config.get('case_6', 'pass_result'):
        logging.info('Case 6 test Pass')
        functions.write_res('Pass', 'result', 6)
    
    else:
        logging.error('Case 6 test Fail')
        functions.write_res('Fail', 'result', 6)
        
    driver.quit()
