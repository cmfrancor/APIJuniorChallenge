import pdb
import requests
import logging as logger


class BackendHelper(object):

    def __init__(self):

        self.baseurl = "https://reqres.in/api"

    def get(self, wc_endpoint, params=None, expected_status_code=200):
        """

        wc_endpoint: Endpoint for the request
        params: Parameters for the request
        expected_status_code: Expected status code for the request
        return: GET request - Returns response_body, status_code and headers
        """
        api = self.baseurl + wc_endpoint
        self.response = requests.get(api, data=params)
        if self.response.status_code == expected_status_code:
            logger.info(f"Successfully retrieved user, Expected status code: {expected_status_code}. "
                        f"Real status code: {self.response.status_code}")
        else:
            raise Exception(f"Bad status code. Expected: {expected_status_code}. Real: {self.response.status_code}")

        return {"response_body": self.response.json(), "status_code": self.response.status_code,
                "response_headers": self.response.headers}

    def post(self, wc_endpoint, params=None, expected_status_code=201):
        """

        wc_endpoint: Endpoint for the request
        params: Parameters for the request
        expected_status_code: Expected status code for the request
        return: POST request - Returns response_body, status_code and headers
        """
        api = self.baseurl + wc_endpoint
        self.response = requests.post(api, data=params)
        if self.response.status_code == expected_status_code:
            logger.info(f"Successfully created user, Expected status code: {expected_status_code}. "
                        f"Real status code: {self.response.status_code}")
        else:
            raise Exception(f"Bad status code. Expected: {expected_status_code}. Real: {self.response.status_code}")

        return {"response_body": self.response.json(), "status_code": self.response.status_code,
                "response_headers": self.response.headers}

    def delete(self, wc_endpoint, params=None, expected_status_code=200):
        """

        wc_endpoint: Endpoint for the request
        params: Parameters for the request
        expected_status_code: Expected status code for the request
        return: DELETE request - Returns response_body, status_code and headers
        """
        api = self.baseurl + wc_endpoint
        self.response = requests.delete(api, data=params)
        if self.response.status_code == expected_status_code:
            logger.info(f"Successfully deleted user, Expected status code: {expected_status_code}. "
                        f"Real status code: {self.response.status_code}")
        else:
            raise Exception(f"Bad status code. Expected: {expected_status_code}. Real: {self.response.status_code}")

        return {"response_body": self.response.json(), "status_code": self.response.status_code,
                "response_headers": self.response.headers}

    def put(self, wc_endpoint, params=None, expected_status_code=200):
        """

        wc_endpoint: Endpoint for the request
        params: Parameters for the request
        expected_status_code: Expected status code for the request
        return: PUT request - Returns response_body, status_code and headers
        """
        api = self.baseurl + wc_endpoint
        self.response = requests.put(api, data=params)
        if self.response.status_code == expected_status_code:
            logger.info(f"Successfully updated user, Expected status code: {expected_status_code}. "
                        f"Real status code: {self.response.status_code}")
        else:
            raise Exception(f"Bad status code. Expected: {expected_status_code}. Real: {self.response.status_code}")
        return {"response_body": self.response.json(), "status_code": self.response.status_code,
                "response_headers": self.response.headers}
