import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
GENDER = "Male"
WEIGHT = "52"
HEIGHT = "171"
AGE = "19"
APP_ID = "ADD YOUR ID HERE"
API_KEY = "ADD YOUR KEY HERE"
exercise_ep = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id" : APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

exercise_txt = input("Tell me the exercises you did today: ")

user_auth = {
    "UserName": "PranavBhat66",
    "Secret": "qwertyuiop"
}

query_params = {
    "query": exercise_txt,
    "gender": GENDER,
    "weight_kg":WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url = f"{exercise_ep}", headers = headers, json = query_params)
result = response.json()
exercise = response.json()['exercises'][0]['name']
duration = response.json()['exercises'][0]['duration_min']
calories = response.json()['exercises'][0]['nf_calories']

sheety_get_ep = "https://api.sheety.co/154f03f6c7ab901817c40641be540029/myWorkouts/workouts"
sheet_post_ep = "https://api.sheety.co/154f03f6c7ab901817c40641be540029/myWorkouts/workouts"


now = datetime.now()

username = "username"
password = "password"

# basic = HTTPBasicAuth(username, password)
# requests.get(sheety_get_ep,auth=basic)

# Usinf basic authentication
for exercise in result["exercises"]:
    body = {
        "workout" : {
            "date" : now.strftime("%d/%m/%Y"),
            "time":now.strftime("%X"),
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
            "Content-Type": "application/json",
        },
        "Content-Type": "application/json",
    }

    post_workout = requests.post(url = sheet_post_ep, json = body, auth = (username, password,))
    print(post_workout.text)