import requests
import functions
import logging
import configparser
import json

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read('config.ini')

def run():
    url = 'https://www.barco.com/bin/barco/product/warranty.json?serialNumber={}'.format(config.get('case_5', 'serial'))

    payload = {}
    headers = {
      'Cookie': 'affinity="334d59ad6b73fa8b"'
    }

    response = requests.request("GET", url, headers=headers, data=payload)


    api_return_dic = {}

    api_return = response.text
    api_return_dic = json.loads(api_return)
    api_return_dic = api_return_dic[0]
    print('api_return_dic = {}'.format(api_return_dic))

    if api_return_dic['serial_number'] == config.get('case_5', 'serial_number') and \
        api_return_dic['part_number'] == config.get('case_5', 'part_number') and \
        api_return_dic['description'] == config.get('case_5', 'description') and \
        api_return_dic['installation_date'] == config.get('case_5', 'installation_date') and \
        api_return_dic['material_number'] == config.get('case_5', 'material_number') and \
        api_return_dic['equipment_number'] == config.get('case_5', 'equipment_number') and \
        api_return_dic['asset_warranty_number'] == config.get('case_5', 'asset_warranty_number') and \
        api_return_dic['asset_warranty_end_date'] == config.get('case_5', 'asset_warranty_end_date') and \
        api_return_dic['asset_warranty_start_date'] == config.get('case_5', 'asset_warranty_start_date') and \
        api_return_dic['delivery_date'] == config.get('case_5', 'delivery_date') and \
        api_return_dic['ecc_sold_to_partner'] == config.get('case_5', 'ecc_sold_to_partner') and \
        api_return_dic['max-service-end-date'] == config.get('case_5', 'max-service-end-date'):
        print('Pass')