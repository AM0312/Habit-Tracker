import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = ""
TOKEN = ""
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
date = datetime(year=2023, month=8, day=21)
UPDATE_ENDPOINT = f"{PIXEL_ENDPOINT}/{date.strftime('%Y%m%d')}"
DELETE_ENDPOINT = UPDATE_ENDPOINT

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_params = {
    "id": GRAPH_ID,
    "name": "My Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(
#     url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)

today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.84"
}

# response = requests.post(
#     url=PIXEL_ENDPOINT, json=pixel_params, headers=headers)
# print(response.text)

update_params = {
    "quantity": "4.1"
}

# response = requests.put(url=UPDATE_ENDPOINT,
#                         json=update_params, headers=headers)
# print(response.text)

response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
print(response.text)
