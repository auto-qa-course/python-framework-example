import os
import json
from lib_custom.common.config_reader import ConfigReader
from lib_custom.common.logger import BaseLogger
from test import outPropertiesPath
import requests


class BaseApi:
    def __init__(self):
        self.test_type = os.environ['TEST_TYPE']

        self.env_name = os.environ['ENVIRONMENT']
        self.env_config = ConfigReader(config_file_path='etc/env{}.conf'.format(self.env_name)).get_configuration()
        self.common_config = ConfigReader(config_file_path='etc/common.conf'.format(self.env_name)).get_configuration()

        self.api_version = self.common_config.get('api_test_parameters', 'api_version')
        self.root_uri = self.env_config.get('api_test_parameters', 'main_api_url')

        ConfigReader(config_file_path=outPropertiesPath).add_configuration(self.test_type.capitalize(),
                                                                           'TEST_URL',
                                                                           self.root_uri)

    @staticmethod
    def post(url, data, **kwargs):
        BaseLogger.write('Sending POST url: {} headers: {} body: {} .'.format(url, kwargs['headers'], data), 'DEBUG')
        response = requests.post(url, data=json.dumps(data), headers=kwargs['headers'])
        BaseLogger.write('Received "{}".'.format(response), 'DEBUG')
        return response

    @staticmethod
    def get(url, **kwargs):
        BaseLogger.write('Sending GET url: {} headers: {}.'.format(url, kwargs['headers']), 'DEBUG')
        response = requests.get(url, headers=kwargs['headers'])
        BaseLogger.write('Received "{}".'.format(response), 'DEBUG')
        return response

    @staticmethod
    def delete(url, **kwargs):
        BaseLogger.write('Sending DELETE url: {} headers: {}.'.format(url, kwargs['headers']), 'DEBUG')
        response = requests.delete(url, headers=kwargs['headers'])
        BaseLogger.write('Received "{}".'.format(response), 'DEBUG')
        return response