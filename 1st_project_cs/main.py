import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

API_KEY = "0654ce6bb73f779a4947205ed003283c"

def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Enter City Name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        print(data)

        if data["cod"] != 200:
            messagebox.showerror("Error", "City Not Found")
            return

        city_label.config(text=f"City: {data['name']}")

        temp_label.config(
            text=f"Temperature: {data['main']['temp']}°C"
        )

        weather_label.config(
            text=f"Condition: {data['weather'][0]['main']}"
        )

        humidity_label.config(
            text=f"Humidity: {data['main']['humidity']}%"
        )

        pressure_label.config(
            text=f"Pressure: {data['main']['pressure']} hPa"
        )

        wind_label.config(
            text=f"Wind Speed: {data['wind']['speed']} m/s"
        )

        sunrise = datetime.fromtimestamp(
            data['sys']['sunrise']
        ).strftime('%H:%M:%S')

        sunset = datetime.fromtimestamp(
            data['sys']['sunset']
        ).strftime('%H:%M:%S')

        sunrise_label.config(
            text=f"Sunrise: {sunrise}"
        )

        sunset_label.config(
            text=f"Sunset: {sunset}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI Window
root = tk.Tk()
root.title("Live Weather Dashboard")
root.geometry("500x500")
root.config(bg="#D6EAF8")

title = tk.Label(
    root,
    text="Live Weather Dashboard",
    font=("Arial", 20, "bold"),
    bg="#D6EAF8"
)
title.pack(pady=10)

city_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=25
)
city_entry.pack(pady=10)

search_btn = tk.Button(
    root,
    text="Search",
    font=("Arial", 12),
    command=get_weather
)
search_btn.pack(pady=10)

city_label = tk.Label(root, text="", font=("Arial", 14), bg="#D6EAF8")
city_label.pack()

temp_label = tk.Label(root, text="", font=("Arial", 14), bg="#D6EAF8")
temp_label.pack()

weather_label = tk.Label(root, text="", font=("Arial", 14), bg="#D6EAF8")
weather_label.pack()

humidity_label = tk.Label(root, text="", font=("Arial", 14), bg="#D6EAF8")
humidity_label.pack()

pressure_label = tk.Label(root, text="", font=("Arial", 14), bg="#D6EAF8")
pressure_label.pack()

wind_label = tk.Label(root, text="", font=("Arial", 14), bg="#D6EAF8")
wind_label.pack()

sunrise_label = tk.Label(root, text="", font=("Arial", 14), bg="#D6EAF8")
sunrise_label.pack()

sunset_label = tk.Label(root, text="", font=("Arial", 14), bg="#D6EAF8")
sunset_label.pack()

root.mainloop()