import allure
from test.api.contacts.test_base_contacts import TestBaseContacts


@allure.story('ST-01 As an FrontEnd developer I want to have API for contact creation so that I can create new contacts.')
class TestCreateContactPositive(TestBaseContacts):

    def setup_method(self):
        TestBaseContacts.setup_method(self)
        self.original_contacts_number = self.contacts_service.get_contacts_number()
        self.create_response = self.contacts_service.post_contact(self.contact_body)
        self.contact_id = self.contacts_service.parse_contact_id(response=self.create_response)

    @allure.testcase('Positive: POST contact - verify 201 response and expected content')
    def test_positive_contact_creation_check_response(self):
        assert self.create_response.status_code == 201
        assert self.contact_id is not None
        assert self.contacts_service.verify_contact_body(self.create_response, self.contact_body)

    @allure.testcase('Positive: POST contact - verify contacts list updated')
    def test_positive_contact_creation_check_list_update(self):
        current_contacts_number = self.contacts_service.get_contacts_number()
        assert self.original_contacts_number + 1 == current_contacts_number

    def teardown_method(self):
        self.contacts_service.delete_contact(self.contact_id)