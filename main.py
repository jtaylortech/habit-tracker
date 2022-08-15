from urllib import request
import requests
from credentials import *

pixela_endpoint = "https://pixe.la/v1/users"

jt_pixela_token = jt_pixela_api
USERNAME = "jtaylortech"


user_params = { 
    "token": jt_pixela_api,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response =requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graphs_config = {
    "id": "graph1",
    "name": "Pages Read",
    "unit": "pages",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": jt_pixela_api 
}

response = requests.post(url=graph_endpoint, json=graphs_config, headers=headers)
print(response.text)