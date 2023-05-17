import requests
import functions
import logging
import configparser

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read('config.ini')

def run():
    url = 'https://www.barco.com/bin/barco/product/warranty.json?serialNumber={}'.format(config.get('case_4', 'serial'))

    payload = {}
    headers = {
      'Cookie': 'affinity="334d59ad6b73fa8b"'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response_time = response.elapsed.total_seconds()

    logging.info('API return time = {} sec'.format(response_time))
    functions.write_res('response_time = {} sec'.format(response_time), 'response', 4)

    if response_time < int(config.get('case_4', 'pass_time')):
        logging.info('Case 4 test Pass')
        functions.write_res('Pass', 'result', 4)

    else:
        logging.error('Case 4 test Fail')
        functions.write_res('Fail', 'result', 4)

