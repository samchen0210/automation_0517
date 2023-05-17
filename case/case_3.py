import logging
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import functions
import time

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read('config.ini')


def run():
    driver = webdriver.Chrome()
    functions.open(driver)
    button = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/form/button')
    
    # serch
    driver.find_element(By.NAME, 'serial').send_keys(config.get('case_3', 'serial'))

    # the button text (clicking)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/form/button').click()
    clicking_button = button.text
    logging.debug('button text = {}'.format(clicking_button))

    # after click
    time.sleep(3)
    after_click = button.text
    logging.debug('button text(after) = {}'.format(after_click))

    functions.write_res('clicking_button={} and after_click={}'.format(clicking_button, after_click), 'response', 3)

    if clicking_button == config.get('case_3', 'clicking_button') and \
        after_click == config.get('case_3', 'after_click'):
        functions.write_res('Pass', 'result', 3)
        logging.info('Case 3 test Pass')

    else:
        functions.write_res('Fail', 'result', 3)
        logging.error('Case 3 test Fail')

    driver.quit()