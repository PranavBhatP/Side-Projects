from datetime import datetime
import requests
import time
MY_LAT = 13.004480
MY_LONG  = 74.791893

def iss_overhead():
    response = requests.get(url = "http://api.open-notify.org/iss-now.json")

    response.raise_for_status()

    iss_longitude = response.json()['iss_position']['longitude']
    iss_latitude = response.json()['iss_position']['latitude']

    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG -5 <= iss_longitude <= MY_LONG + 5

def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
    }

    response = requests.get(url  = "https://api.sunrise-sunset.org/json", params = parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    time_now = datetime.now().hour #"hour" attribute of datetime function.

    return (time_now >= sunset or time_now <= sunrise)
while True:
    time.sleep(60)    
    if iss_overhead and is_night():
        print("THE ISS IS ABOV YOUR LOCATION!, LOOK UP!")
