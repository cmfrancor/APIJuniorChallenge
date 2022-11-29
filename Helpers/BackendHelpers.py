import pdb
import requests


class BackendHelper(object):

    def __init__(self):

        self.baseurl="https://reqres.in/api"

    def get(self, wc_endpoint, params=None, expected_status_code=200):
        """

        :param wc_endpoint: Endpoint for the request
        :param params: Parameters for the request
        :param expected_status_code: Expected status code for the request
        :return: GET request
        """
        api = self.baseurl + wc_endpoint
        self.response = requests.get(api, data=params)
        if self.response.status_code == expected_status_code:
            print(f"Sucessfully created user, Expected status code: {expected_status_code}. Real status code: {self.response.status_code}")
        else:
            raise Exception(f"Bad status code. Expected: {expected_status_code}. Real: {self.response.status_code}")

        return {"response_body": self.response.json(), "status_code": self.response.status_code,
                "response_headers": self.response.headers}

    def post(self, wc_endpoint, params=None, expected_status_code=201):
        """

        :param wc_endpoint: Endpoint for the request
        :param params: Parameters for the request
        :param expected_status_code: Expected status code for the request
        :return: POST request
        """
        api = self.baseurl + wc_endpoint
        self.response = requests.post(api, data=params)
        if self.response.status_code == expected_status_code:
            print("           ")
            print(f"Endpoint called as expected, Expected status code: {expected_status_code}. Real status code: {self.response.status_code}")
            print("           ")
        else:
            raise Exception(f"Bad status code. Expected: {expected_status_code}. Real: {self.response.status_code}")

        return {"response_body": self.response.json(), "status_code": self.response.status_code,
                "response_headers": self.response.headers}

    def delete(self, wc_endpoint, params=None, expected_status_code=200):
        """

        :param wc_endpoint: Endpoint for the request
        :param params: Parameters for the request
        :param expected_status_code: Expected status code for the request
        :return: DELETE request
        """
        api = self.baseurl + wc_endpoint
        self.response = requests.delete(api, data=params)
        if self.response.status_code == expected_status_code:
            print(f"Sucessfully created user, Expected status code: {expected_status_code}. Real status code: {self.response.status_code}")
        else:
            raise Exception(f"Bad status code. Expected: {expected_status_code}. Real: {self.response.status_code}")

        return {"response_body": self.response.json(), "status_code": self.response.status_code,
                "response_headers": self.response.headers}

    def put(self, wc_endpoint, params=None, expected_status_code=200):
        """

        :param wc_endpoint: Endpoint for the request
        :param params: Parameters for the request
        :param expected_status_code: Expected status code for the request
        :return: PUT request
        """
        api = self.baseurl + wc_endpoint
        self.response = requests.put(api, data=params)
        if self.response.status_code == expected_status_code:
            print(f"Sucessfully created user, Expected status code: {expected_status_code}. Real status code: {self.response.status_code}")
        else:
            raise Exception(f"Bad status code. Expected: {expected_status_code}. Real: {self.response.status_code}")
        return {"response_body": self.response.json(), "status_code": self.response.status_code,
                "response_headers": self.response.headers}
