import os
from lib_custom.common.config_reader import ConfigReader
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test import outPropertiesPath
from lib_custom.common.logger import BaseLogger


class SeleniumDriverCover():

    def __init__(self, *args, **kwargs):
        self.browser_type = kwargs['browser_type']

    def start_driver(self):
        BaseLogger.write('Loaded browser configuration: {}'.format(self.browser_type))

        if self.browser_type == 'firefox':
            current_driver = webdriver.Firefox()
        elif self.browser_type == 'chrome_headless':
            current_driver = self.setup_chrome_driver_headless()
        elif self.browser_type == 'chrome':
            current_driver = webdriver.Chrome()
        else:
            raise ValueError("Not expected browser type specified.")

        BaseLogger.write('Successfully loaded Webdriver.')
        return current_driver

    def setup_chrome_driver_headless(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        if 'CHROME_CANARY_PATH' in os.environ.keys():
            chrome_options.binary_location = os.path.abspath(os.environ['CHROME_CANARY_PATH'])
        else:
            BaseLogger.write('Entered setup headless without canary.')
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
        return webdriver.Chrome(chrome_options=chrome_options)


if ('BROWSER' in os.environ.keys()) and (os.environ['BROWSER'] is not None):
    browser_type = os.environ['BROWSER'].lower()
else:
    browser_type = 'chrome'

ConfigReader(config_file_path=outPropertiesPath).add_configuration('UI', 'BROWSER', browser_type)



