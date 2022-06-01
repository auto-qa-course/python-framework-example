from lib_custom.api.base_api import BaseApi


class ContactsApi(BaseApi):

    def __init__(self):
        BaseApi.__init__(self)
        self.resource_path = self.common_config.get('api_test_parameters', 'contacts_endpoint')
        self.contacts_url = '{}{}{}'.format(self.root_uri, self.api_version, self.resource_path)
        self.default_headers = {'Content-Type': 'application/json'}

    def post_contact(self, contact_body):
        response = self.post(self.contacts_url, contact_body, headers=self.default_headers)
        return response

    def get_contact_by_id(self, contact_id):
        url = '{}/{}'.format(self.contacts_url, contact_id)
        response = self.get(url, headers=self.default_headers)
        return response

    def get_contacts_list(self):
        response = self.get(self.contacts_url, headers=self.default_headers)
        return response

    def delete_contact(self, contact_id):
        url = '{}/{}'.format(self.contacts_url, contact_id)
        response = self.delete(url, headers=self.default_headers)
        return response

    def parse_contact_id(self, **kwargs):
        parsed_content = self.parse_response_json(kwargs['response'])
        return parsed_content[0]['id']