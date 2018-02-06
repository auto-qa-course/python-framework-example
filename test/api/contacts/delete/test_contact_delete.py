import allure
from test.api.contacts.test_base_contacts import TestBaseContacts


@allure.story('ST-02 As an FrontEnd developer I want to have API for contact delete so that I can remove not needed contacts.')
class TestDeleteContact(TestBaseContacts):

    def setup_method(self):
        TestBaseContacts.setup_method(self)
        self.original_contacts_number = self.contacts_service.get_contacts_number()
        self.contact_id = self.contacts_service.create_new_contact_get_id(self.contact_body)

    @allure.testcase('Positive: Delete contact - verify contacts list updated')
    def test_positive_contact_delete(self):
        response = self.contacts_service.delete_contact(self.contact_id)
        assert response.status_code == 200

        contacts_list_response = self.contacts_service.get_contacts_list()
        parsed_content = self.contacts_service.parse_response_json(contacts_list_response)
        current_contacts_number = len(parsed_content)

        assert self.original_contacts_number == current_contacts_number
