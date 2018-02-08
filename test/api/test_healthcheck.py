from test.api.test_base import TestBase
from lib_custom.api.base_api import BaseApi


class TestHealthcheck(TestBase):

    def test_positive_contact_creation_check_response(self):
        base_api = BaseApi()
        url = '{}/healthcheck'.format(base_api.root_uri)
        response = base_api.get(url, headers={})
        assert response.status_code == 200
        assert response._content == 'live'
