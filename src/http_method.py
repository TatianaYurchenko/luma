import os
import requests
from dotenv import load_dotenv
load_dotenv()
class MyRequests:

    def get(self, url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return self.__send(url, data, headers, cookies, method="GET")

    def post(self, url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return self.__send(url, data, headers, cookies, method="POST")

    def put(self, url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return self.__send(url, data, headers, cookies, method="PUT")

    def delete(self, url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return self.__send(url, data, headers, cookies, method="DELETE")


    @staticmethod
    def __send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        HOST = os.environ.get("HOST")
        base_url = f"""{HOST}{url}"""

        if headers is None:
            headers = {"Content-Type": "application/json"}
        if cookies is None:
            cookies = {}

        try:
            response = requests.request(
                method=method,
                url=base_url,
                data=data,
                headers=headers,
                cookies=cookies
            )
            return response
        except Exception as e:
            raise e
