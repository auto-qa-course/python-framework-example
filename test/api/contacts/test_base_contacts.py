from allure import feature
from test.api.test_base import TestBase
from lib_custom.api.contacts.contacts_api import ContactsApi


@feature('Contacts API')
class TestBaseContacts(TestBase):

    def setup_class(self):
        self.contacts_api = ContactsApi()