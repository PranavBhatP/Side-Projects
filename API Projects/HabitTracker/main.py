import requests
import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME   ="Add username here"
TOKEN = "ADD TOKEN HERE"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url = pixela_endpoint, json = user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph2",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}


# response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
# print(response.text)

today = datetime.datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "100",
}

# pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

# response = requests.post(url  = pixel_endpoint, json = pixel_config, headers = headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{pixel_config['date']}"

new_pixel_data = {
    "quantity": "60",    
}

response  = requests.put(url = update_endpoint, json = new_pixel_data, headers = headers)
print(response.text)