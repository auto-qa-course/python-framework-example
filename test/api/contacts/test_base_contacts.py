from allure import feature
from test.api.test_base import TestBase
from lib_custom.api.contacts.contacts_service import ContactsService
from lib_custom.api.contacts.contacts_test_data import ContactsTestData


@feature('Contacts API')
class TestBaseContacts(TestBase):

    def setup_class(self):
        self.contacts_service = ContactsService()

    def setup_method(self):
        self.contact_body = ContactsTestData.generate_valid_contact_data()