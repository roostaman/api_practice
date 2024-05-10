import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = "__YOUR_TWILIO_ACCOUNT_ID__"
auth_token = "__YOUR_TWILIO_AUTH_TOKEN__"

MY_LAT = 45.140162
MY_LNG = 75.363642

api_key = os.environ.get("OWM_API_KEY")
parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
}
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_list = weather_data["list"]

will_rain = False
for num in weather_list:
    rain_code = num["weather"][0]["id"]
    if rain_code < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)
