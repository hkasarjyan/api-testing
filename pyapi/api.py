import requests
import json


class APICalls:
    def __init__(self, url, get_params=None, post_data=None, post_json_data=None, put_params=None, delete_params=None):
        self.url = url
        self.get_params = get_params
        self.post_data = post_data
        self.post_json_data = post_json_data
        self.put_params = put_params
        self.delete_params = delete_params

    # GET method
    def get(self, **kwargs):
        response = requests.get(self.url, params=self.get_params, **kwargs)
        return response

    def get_response_code(self):
        response = requests.get(self.url, params=self.get_params)
        return response.status_code

    def get_content(self):
        response = requests.get(self.url, params=self.get_params)
        return response.content

    def get_headers(self):
        response = requests.get(self.url, params=self.get_params)
        return response.headers

    def get_text(self):
        response = requests.get(self.url, params=self.get_params)
        return response.text

    def get_request(self):
        response = requests.get(self.url, params=self.get_params)
        return response.request

    def get_json(self):
        response = requests.get(self.url, params=self.get_params)
        return response.json()

    # POST method
    def post(self, **kwargs):
        response = requests.post(self.url, data=self.post_data, **kwargs)
        return response

    def post_response_code(self):
        response = requests.post(self.url, data=self.post_data)
        return response.status_code

    def post_content(self):
        response = requests.post(self.url, data=self.post_data)
        return response.content

    def post_headers(self):
        response = requests.post(self.url, data=self.post_data)
        return response.headers

    def post_text(self):
        response = requests.post(self.url, data=self.post_data)
        return response.text

    def post_request(self):
        response = requests.post(self.url, data=self.post_data)
        return response.request

    def post_json(self):
        response = requests.post(self.url, data=self.post_data, json=self.post_json_data)
        return response.json()

    # PUT method
    def put(self, **kwargs):
        response = requests.put(self.url, params=self.put_params, **kwargs)
        return response

    def put_response_code(self):
        response = requests.put(self.url, params=self.put_params)
        return response.status_code

    def put_content(self):
        response = requests.put(self.url, params=self.put_params)
        return response.content

    def put_headers(self):
        response = requests.put(self.url, params=self.put_params)
        return response.headers

    def put_text(self):
        response = requests.put(self.url, params=self.put_params)
        return response.text

    def put_request(self):
        response = requests.put(self.url, params=self.put_params)
        return response.request

    def put_json(self):
        response = requests.put(self.url, params=self.put_params)
        return response.json()

    # DELETE method
    def delete(self, **kwargs):
        response = requests.delete(self.url, params=self.delete_params, **kwargs)
        return response

    def delete_response_code(self):
        response = requests.delete(self.url, params=self.delete_params)
        return response.status_code

    def delete_content(self):
        response = requests.delete(self.url, params=self.delete_params)
        return response.content

    def delete_headers(self):
        response = requests.delete(self.url, params=self.delete_params)
        return response.headers

    def delete_text(self):
        response = requests.delete(self.url, params=self.delete_params)
        return response.text

    def delete_request(self):
        response = requests.delete(self.url, params=self.delete_params)
        return response.request

    def delete_json(self):
        response = requests.delete(self.url, params=self.delete_params)
        return response.json()