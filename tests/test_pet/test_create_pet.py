import allure
import pytest
from data import get_pet_endpoints
from src.assertions import Assertions
from src.http_method import MyRequests
from http import HTTPStatus
import os


@allure.epic("Test create pet")
class TestCreatePet:
    request = MyRequests()
    url = get_pet_endpoints()
    assertions = Assertions()

    def test_create_pet(self, get_test_name):
        data = """{
          "id": 12,
          "category": {
            "id": 56,
            "name": "string7879"
          },
          "name": "doggie",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 5,
              "name": "string"
            }
          ],
          "status": "available"
        }"""
        response = self.request.post(url=self.url.create_pet, data=data)
        self.assertions.assert_status_code(
            response=response,
            actual_status_code=HTTPStatus.CREATED,
            test_name=get_test_name)
        # print(os.environ)
        # print(response.text)
        print(f' response{response}')
        print(f' response{HTTPStatus.CREATED}')
        print(f' response{get_test_name}')
