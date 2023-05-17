import configparser
import logging
from logging.handlers import RotatingFileHandler
import sys
import case.case_1
import case.case_2
import case.case_3
import case.case_4
import case.case_5

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read('config.ini')

logging.basicConfig(
level=logging.DEBUG,
format="%(asctime)s – [line:%(lineno)d] – %(levelname)s: %(message)s",
handlers=[
    logging.handlers.RotatingFileHandler('tester.log', maxBytes=100000, backupCount=5),
    logging.StreamHandler(sys.stdout)
])


if __name__ == '__main__':
   
    for i in range(1, 20):
        if config.get('run_case', 'case_{}'.format(i)) == 'true':
            logging.info('Run Case {}'.format(i))
            case_to_run = getattr(case, 'case_{}'.format(i))
            case_to_run.run()

    
    logging.info('Test end !!!!!!!!!!!!!')