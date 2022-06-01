import allure
import pytest
from test.api.contacts.test_base_contacts import TestBaseContacts


@allure.story('ST-01 As an FrontEnd developer I want to have API for contact creation so that I can create new contacts.')
class TestCreateContactNegative(TestBaseContacts):

    @allure.step('Negative: POST contact with missing Email - verify 400')
    @pytest.mark.xfail
    def test_negative_meeting_creation_without_email(self):
        contact_body = self.contact_body
        del contact_body['email']
        response = self.contacts_service.post_contact(contact_body)
        assert response.status_code == 400

    @allure.step('Negative: POST contact with missing firstName - verify 400')
    @pytest.mark.xfail
    def test_negative_meeting_creation_without_first_name(self):
        contact_body = self.contact_body
        del contact_body['firstName']
        response = self.contacts_service.post_contact(contact_body)
        assert response.status_code == 400

    @allure.step('Negative: POST contact with missing lastName - verify 400')
    @pytest.mark.xfail
    def test_negative_meeting_creation_without_last_name(self):
        contact_body = self.contact_body
        del contact_body['lastName']
        response = self.contacts_service.post_contact(contact_body)
        assert response.status_code == 400

    @allure.step('Negative: POST contact with not proper Email - verify 400')
    @pytest.mark.xfail
    def test_negative_meeting_creation_with_not_proper_email(self):
        contact_body = self.contact_body
        contact_body['email'] = 'test.email.com'
        response = self.contacts_service.post_contact(contact_body)
        assert response.status_code == 400

    @allure.step('Negative: POST contact with not JSON format - verify 400')
    @pytest.mark.xfail
    def test_negative_meeting_creation_with_not_proper_format(self):
        response = self.contacts_service.post_contact(self.contact_body['email'])
        assert response.status_code == 400

    @allure.step('Negative: POST contact with empty body - verify 400')
    @pytest.mark.xfail
    def test_negative_meeting_creation_with_empty_body(self):
        response = self.contacts_service.post_contact({})
        assert response.status_code == 400