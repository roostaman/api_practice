import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 51
MY_LON = 71

MY_EMAIL = "qwerty@qwerty.com"
MY_PASSWORD = "qwertyqwertyqwerty"
R_EMAIL = "azerty@azerty.com"

response_1 = requests.get(url="http://api.open-notify.org/iss-now.json")
response_1.raise_for_status()
longitude = float(response_1.json()['iss_position']['longitude'])
latitude = float(response_1.json()['iss_position']['latitude'])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
}

response = requests.get(url="https://api.sunrisesunset.io/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split(":")[:2]
sunset = data["results"]["sunset"].split(":")[:2]

now = datetime.now()
current_time = [now.hour, now.minute]

while True:
    time.sleep(60)
    if current_time[0] > int(sunrise[0]):
        if longitude in range(MY_LON - 5, MY_LON + 5) and latitude in range(MY_LAT - 5, MY_LAT + 5):
            print("It's time!")

            with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as server:
                server.login(user=MY_EMAIL, password=MY_PASSWORD)
                server.sendmail(from_addr=MY_EMAIL, to_addrs=R_EMAIL,
                                msg="Subject:Yo, Look UP!\n\nThe ISS is above you.")
                break
