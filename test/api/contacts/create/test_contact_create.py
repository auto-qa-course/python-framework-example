import allure
from test.api.contacts.test_base_contacts import TestBaseContacts
from lib_custom.common.test_data_generators import TestDataGenerators


@allure.story('ST-01 As an FrontEnd developer I want to have API for contact creation so that I can create new contacts.')
class TestCreateContact(TestBaseContacts):

    random_string = TestDataGenerators.generate_random_str(8)

    def setup_method(self):
        response = self.contacts_api.get_contacts_list()
        parsed_content = self.contacts_api.parse_response_json(response)
        self.original_contacts_number = len(parsed_content)

        contact_body = {'email': 'test.{}@email.com'.format(self.random_string),
                        'firstName': 'Name{}'.format(self.random_string),
                        'lastName': 'LastName{}.'.format(self.random_string)}
        self.create_response = self.contacts_api.post_contact(contact_body)

    @allure.testcase('Positive: POST meeting - verify 201 response and expected content')
    def test_positive_meeting_creation_check_response(self):
        assert self.create_response.status_code == 201

        contact_id = self.contacts_api.parse_contact_id(response=self.create_response)
        assert contact_id is not None

    @allure.testcase('Positive: POST meeting - verify contacts list updated')
    def test_positive_meeting_creation_check_list_update(self):
        contacts_list_response = self.contacts_api.get_contacts_list()
        parsed_content = self.contacts_api.parse_response_json(contacts_list_response)
        current_contacts_number = len(parsed_content)

        assert self.original_contacts_number + 1 == current_contacts_number

    def teardown_method(self):
        contact_id = self.contacts_api.parse_contact_id(response=self.create_response)
        self.contacts_api.delete_contact(contact_id)