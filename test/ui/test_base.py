import pytest
import sys
from allure_commons.types import AttachmentType
from lib_custom.common.logger import BaseLogger
from test.ui import browser_type
from test.ui import SeleniumDriverCover


@pytest.allure.feature('')
class TestBase:

    def setup_class(self):
        self.driver = SeleniumDriverCover(browser_type=browser_type).start_driver()

    def teardown_class(self):
        self.driver.quit()
        BaseLogger.write('Driver quit successful.')

    def teardown_method(self):
        if not sys.exc_info()[0]:
            pytest.allure.attach(name='screenshot',
                                 body=self.driver.get_screenshot_as_png(),
                                 attachment_type=AttachmentType.PNG,
                                 extension='png')
            pytest.allure.attach(name='html_content',
                                 body=self.driver.page_source,
                                 attachment_type=AttachmentType.HTML,
                                 extension='html')
            pytest.allure.attach(name='browser_log',
                                 body=str(self.driver.get_log('browser')),
                                 attachment_type=AttachmentType.TEXT,
                                 extension='txt')