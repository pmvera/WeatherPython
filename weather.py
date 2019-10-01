# -*- coding: utf-8 -*-

import requests
from Tkinter import *

city_id = {"Madrid" : 6359304, "Arroyomolinos" : 3129356}

class Weather:
    def main(self):
        city = self.city_listbox.get()
        id = city_id.get(city)
        url = "https://samples.openweathermap.org/data/2.5/weather?id={}&appid=b6907d289e10d714a6e88b30761fae22".format(id)
        res = requests.get(url)
        output = res.json()

        weather_status = str(output['weather'][0]['description'])
        temperature = str(float(output['main']['temp']) - 273.0) + " ºC"
        humidity = str(output['main']['humidity']) + "%"
        wind_speed = str(output['wind']['speed']) + " m/s"

        self.weather_status_label.configure(text="weather_status: " + weather_status)
        self.temperature_status_label.configure(text="temperature: " + temperature)
        self.humidity_status_label.configure(text="humidity: " + humidity)
        self.wind_speed_status_label.configure(text="wind_speed: " + wind_speed)

    def __init__(self):
        window = Tk()
        window.geometry("400x350")

        city_name_list = ["Madrid", "Arroyomolinos"]
        self.city_listbox = StringVar(window)
        self.city_listbox.set("Select de city")
        option = OptionMenu(window, self.city_listbox, *city_name_list)
        option.grid(row=2, column=2, padx=150, pady=10)

        b1 = Button(window, text="Check weather", width=15, command=self.main)
        b1.grid(row=5, column=2, padx=150)

        self.weather_status_label = Label(window, font=("times", 10, "bold"))
        self.weather_status_label.grid(row=10, column=2)

        self.temperature_status_label = Label(window, font=("times", 10, "bold"))
        self.temperature_status_label.grid(row=12, column=2)

        self.humidity_status_label = Label(window, font=("times", 10, "bold"))
        self.humidity_status_label.grid(row=14, column=2)

        self.wind_speed_status_label = Label(window, font=("times", 10, "bold"))
        self.wind_speed_status_label.grid(row=16, column=2)
        window.mainloop()

if __name__ == '__main__':
    wth = Weather()
