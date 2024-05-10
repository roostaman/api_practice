import requests
import datetime as dt
import os

# nutritionix keys and config
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

track_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
track_params = {
    "query": input("Tell which exercises you did: ")
}
response = requests.post(url=track_endpoint, headers=headers, json=track_params)
response.raise_for_status()
data_ex = response.json()["exercises"][0]

today = dt.datetime.now()
today_date = today.date().strftime("%d/%m/%Y")
time_now = today.time().strftime("%H:%M:%S")


# sheety api config
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
SHEET_USERNAME = os.environ.get("SHEET_USERNAME")
SHEET_PASSWORD = os.environ.get("PASSWORD")
SHEET_TOKEN = os.environ.get("SHEET_TOKEN")

headers_sheety = {
    "Authorization": SHEET_TOKEN,
    "Username": SHEET_USERNAME,
    "Password": SHEET_PASSWORD
}

# for each exercise entered
for exc in data_ex:
    exercise = data_ex["name"]
    duration = data_ex["duration_min"]
    calories = data_ex["nf_calories"]

    sheety_params = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }
    response_sheety = requests.post(
        url=SHEET_ENDPOINT,
        json=sheety_params,
        headers=headers_sheety
    )
    print(response_sheety.status_code)
