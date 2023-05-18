import logging
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import functions

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read('config.ini')


def run():
    driver = webdriver.Chrome()
    functions.open(driver)
    
    wait = WebDriverWait(driver, 5)
    accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept All Cookies')]")))
    accept_button.click()

    wait = WebDriverWait(driver, 5)
    accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept All Cookies')]")))
    accept_button.click()
    
    button = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/form/button')
    original_color = button.value_of_css_property('background-color')
    logging.debug('original_color = {}'.format(original_color))

    actions = ActionChains(driver)
    actions.move_to_element(button).perform()

    hover_color = button.value_of_css_property('background-color')
    logging.debug('hover_color = {}'.format(hover_color))
    
    functions.write_res('original_color={} and hover_color={}'.format(original_color, hover_color), 'response', 2)

    if hover_color != original_color:
        functions.write_res('Pass', 'result', 2)
        logging.info('Case 2 test Pass')

    else:
        functions.write_res('Fail', 'result', 2)
        logging.error('Case 2 test Fail')

    driver.quit()