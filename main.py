from urllib import request
import requests
from credentials import *

pixela_endpoint = "https://pixe.la/v1/users"

jt_pixela_token = jt_pixela_api
USERNAME = "jtaylortech"
READING_GRAPH = "graph1"


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
    "id": READING_GRAPH,
    "name": "Pages Read",
    "unit": "pages",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": jt_pixela_api 
}

# response = requests.post(url=graph_endpoint, json=graphs_config, headers=headers)
# print(response.text)

pixels_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{READING_GRAPH}"

pixels_config = {
    "date": "20220815",
    "quantity": "36.2",
}

response = requests.post(url=pixels_endpoint, json=pixels_config, headers=headers)
print(response.text)

