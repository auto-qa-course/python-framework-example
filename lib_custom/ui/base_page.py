from page_objects import PageObject
import os
from lib_custom.common.config_reader import ConfigReader


class BasePage(PageObject):

    def __init__(self, *args, **kwargs):
        self.env_name = os.environ['ENVIRONMENT']
        self.env_config = ConfigReader(config_file_path='etc/env{}.conf'.format(self.env_name)).get_configuration()
        kwargs['root_uri'] = self.env_config.get('ui_test_parameters', 'ui_url')

        PageObject.__init__(self, *args, **kwargs)