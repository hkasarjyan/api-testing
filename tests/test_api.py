import pytest
from pyapi.api import APICalls
from util.conftest import *


class TestAPI:
    url = "https://google.com"
    get_params = None
    post_data = None
    post_json_data = None
    put_params = None
    delete_params = None

    def test_get_method(self):
        api = APICalls(self.url, get_params=self.get_params)
        assert api.get_response_code() == 200
        assert api.get_text() is not None
        assert api.get_content() is not None
        assert api.get_headers() is not None

    def test_post_method(self):
        api = APICalls(self.url, post_data=self.post_data, post_json_data=self.post_json_data)
        assert api.post_response_code() == 200
        assert api.post_text() is not None
        assert api.post_content() is not None
        assert api.post_headers() is not None
        assert api.post_json() is not None

    def test_put_method(self):
        api = APICalls(self.url, put_params=self.put_params)
        assert api.put_response_code() == 200
        assert api.put_text() is not None
        assert api.put_content() is not None
        assert api.put_headers() is not None
        assert api.put_json() is not None

    def test_delete_method(self):
        api = APICalls(self.url, delete_params=self.delete_params)
        assert api.delete_response_code() == 200
        assert api.delete_text() is not None
        assert api.delete_content() is not None
        assert api.delete_headers() is not None
        assert api.delete_json() is not None
