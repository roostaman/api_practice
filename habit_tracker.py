import requests
import datetime as dt

# 1.Create your user account
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "roostaman"
TOKEN = "zhdorkdnshkhwejahodndsha"

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_params)
# response.raise_for_status()
# print(response.text)


# 2.Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "RunningGraph",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# 3.Get the graph by:  /v1/users/<username>/graphs/<graphID>

today_date = dt.date.today()
formatted_date = today_date.strftime("%Y%m%d")

# 4.Post value to the graph
update_value_endpoint = f"{graph_endpoint}/graph1"
value_params = {
    "date": formatted_date,
    "quantity": "15.9"
}
# response = requests.post(url=update_value_endpoint, headers=headers, json=value_params)
# print(response.text)

# New value
# response = requests.post(url=update_value_endpoint, headers=headers, json=value_params)

# 5.Updating posted pixel info PUT method
new_value = f"{update_value_endpoint}/{formatted_date}"
new_value_params = {
    "quantity": "10.2",
    "something": "3.3"
}
# response = requests.put(url=new_value, headers=headers, json=new_value_params)
# print(response.text)

# 6.Deleting data delete
response = requests.delete(url=new_value, headers=headers)
print(response.text)
