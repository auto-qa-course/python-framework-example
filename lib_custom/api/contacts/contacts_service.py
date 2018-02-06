from lib_custom.api.contacts.contacts_api import ContactsApi


class ContactsService(ContactsApi):

    def __init__(self):
        ContactsApi.__init__(self)

    def get_contacts_number(self):
        response = self.get_contacts_list()
        parsed_content = self.parse_response_json(response)
        return len(parsed_content)

    def create_new_contact_get_id(self, contact_body):
        response = self.post_contact(contact_body)
        contact_id = self.parse_contact_id(response=response)
        return contact_id