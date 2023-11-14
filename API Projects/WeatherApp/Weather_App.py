# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:15:42 2020

@author: Dell
"""

import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

def test_button(entry):
    print("This is the entry: ", entry)
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
#e99b40640d9df3faa805c81e75874f8f

def format_response(weather):
    try:
        name = (weather['name'])
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
    
        final_str = "City : %s\nConditions: %s\nTemperature(C): %s" % (name, description, round(5/9*(temp-32)))
    except:
        final_str = 'There was a problem to retrieve that info.'
    return final_str
def get_weather(city):
    weather_key = 'e99b40640d9df3faa805c81e75874f8f'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q' : city, 'units': 'imperial'}
    response = requests.get(url, params= params)
    weather = response.json()
    label['text'] = format_response(weather)
   
    
root = tk.Tk()
root.title("Weather App")

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

bg_img = tk.PhotoImage(file = 'C:/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/API Projects/WeatherApp/landscape.png')
bg_label = tk.Label(root, image = bg_img)
bg_label.place(relwidth = 1, relheight =1)

frame = tk.Frame(root, bg = '#80bfff', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

button = tk.Button(frame, text = "Get Weather", font =("Microsoft Uighur", 15), command = lambda: get_weather(entry.get()))
button.place(relx = 0.7, relwidth = 0.3, relheight = 1)

entry = tk.Entry(frame, font = ("Microsoft Uighur", 16))
entry.place(relwidth =0.65, relheight = 1)

lower_frame = tk.Frame(root, bg = "#80bfff", bd = 5)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

label = tk.Label(lower_frame, font  = ("Microsoft Uighur", 20), anchor  ='nw',justify = 'left', bd= 4)
label.place(relwidth = 1, relheight = 1)
#print(tk.font.families())

root.mainloop()
