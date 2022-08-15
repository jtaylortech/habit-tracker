import requests
from credentials import *

pixela_endpoint = "https://pixe.la/v1/users"

jt_pixela_token = jt_pixela_api


user_params = { 
    "token": jt_pixela_api,
    "username": "jtalortech",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response =requests.post(url=pixela_endpoint,json=user_params)
print(response.text)