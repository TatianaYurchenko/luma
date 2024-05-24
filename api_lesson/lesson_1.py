import requests
from requests.auth import HTTPBasicAuth
def first_request():
    response = requests.get("https://petstore.swagger.io/")
    print(response)

def heder_parametrs():
    # параметры get запроса
    response = requests.get(
        url="", # end point
        # auth=HTTPBasicAuth("USERNAME", "PASSWORD")
        headers={},
        params={},
        verify=False
    )
#  Задача получить инвентврь
def auth_with_api_key():
    response = requests.get(
        url="https://petstore.swagger.io/v2/store/inventory", # end point
        headers={
            "api_key": "special-key"
        }
    )
    print(response.json()['sold'])
    print(response.status_code)

def get_request_with_query_parametrs():
    response = requests.get(
        url="https://petstore.swagger.io/v2/pet/findByStatus",  # end point
        headers={
            "api_key": "special-key"
        },
        params={
            "status": "sold"
        }
    )
    print(response.json())

def post_add_animal():
    response = requests.post(
        url='https://petstore.swagger.io/v2/pet',  # end point
        headers={
            "api_key": "special-key"
        },
        json={
              "id": 101,
              "category": {
                "id": 0,
                "name": "string"
              },
              "name": "doggie",
              "photoUrls": [
                "string"
              ],
              "tags": [
                {
                  "id": 0,
                  "name": "Dogs"
                }
              ],
              "status": "available"
            })
    print(response)
def get_pet_by_id():
    get_by_id = requests.get(url='https://petstore.swagger.io/v2/pet/101',
                            headers={
                                "api_key": "special-key"
                            }
                            )
    print(get_by_id.json())

def post_add_image():
    response = requests.post(
        url='https://petstore.swagger.io/v2/pet/101/uploadImage',  # end point
        headers={
            "api_key": "special-key"
        },
        files={
            "file": ("котик.jpg", open("котик.JPG", "rb"), "image/jpeg")
        })
    print(response.status_code)
    print(response.json())

post_add_image()

