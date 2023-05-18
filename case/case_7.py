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

    response = {}
    result_list = []

    for i in range(1, 25):
        word = config.get('case_7', 'input_{}'.format(i))
        driver.find_element(By.NAME, 'serial').send_keys(word)
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/form/button').click()
        time.sleep(2)

        status = driver.find_element(By.XPATH, '//*[@id="serial"]/following-sibling::div').text
        logging.info('Keyin {} , web returns = {}'.format(word, status))

        response[word] = status

        if status == config.get('case_7', 'pass_result'):
            result_list.append('pass')
        else:
            result_list.append('fail')

        driver.refresh()
        time.sleep(1)


    functions.write_res(response, 'response', 7)
    logging.info('Got result = {}'.format(response))

    if not 'fail' in result_list:
        functions.write_res('Pass', 'result', 7)
        logging.info('Case 7 test Pass')
    else:
        functions.write_res('Fail', 'result', 7)
        logging.error('Case 7 test Fail')
        
    driver.quit()
