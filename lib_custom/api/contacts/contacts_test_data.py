from lib_custom.api.contacts.contacts_api import ContactsApi
from lib_custom.common.test_data_generators import TestDataGenerators


class ContactsTestData():

    @staticmethod
    def generate_valid_contact_data():
        random_string = TestDataGenerators.generate_random_str(8)
        contact_body = {'email': 'test.{}@email.com'.format(random_string),
                        'firstName': 'Name{}'.format(random_string),
                        'lastName': 'LastName{}.'.format(random_string)}
        return contact_body
