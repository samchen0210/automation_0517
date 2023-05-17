import logging
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import functions

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read('config.ini')

def run():
    driver = webdriver.Chrome()
    functions.open(driver)
    
    # serch
    driver.find_element(By.NAME, 'serial').send_keys(config.get('case_1', 'serial'))
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/form/button').click()
    time.sleep(3)

    # read result
    dl_element = driver.find_element(By.TAG_NAME, 'dl')
    dt_elements = dl_element.find_elements(By.TAG_NAME, 'dt')

    res = {}

    for dt_element in dt_elements:
        dt_content = dt_element.text
        dd_elements = dt_element.find_elements(By.XPATH, "./following-sibling::dd[1]")
        dd_content = [dd.text for dd in dd_elements]
        dd_content = dd_content[0]
        res[dt_content] = dd_content

    logging.info('Got result = {}'.format(res))

    functions.write_res(res, 'response', 1)
    
    if config.get('case_1', 'Description') == res['Description'] and \
        config.get('case_1', 'Part_number') == res['Part number'] and \
        config.get('case_1', 'Installation_date') == res['Installation date'] and \
        config.get('case_1', 'Warranty_end_date') == res['Warranty end date']:
        
        functions.write_res('Pass', 'result', 1)
        logging.info('Case 1 test Pass')
    
    else:
        functions.write_res('Fail', 'result', 1)
        logging.error('Case 1 test fail')
        
    driver.quit()
