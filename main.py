import tkinter as tk
from tkinter import messagebox
import requests
import json

# API key aur base url
API_KEY = "36e1c7c4d4b44b1daab14641250909"
BASE_URL = "https://api.weatherapi.com/v1/current.json"

# Function to get weather
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    try:
        url = f"{BASE_URL}?key={API_KEY}&q={city}"
        response = requests.get(url)
        data = json.loads(response.text)

        if "error" in data:
            messagebox.showerror("Error", f"City '{city}' not found!")
            return

        # Weather details
        temp = data["current"]["temp_c"]
        feels = data["current"]["feelslike_c"]
        humidity = data["current"]["humidity"]
        cloud = data["current"]["cloud"]
        condition = data["current"]["condition"]["text"]

        # Update labels
        result_label.config(
            text=f"🌡 Temperature: {temp} °C\n"
                 f"🤔 Feels Like: {feels} °C\n"
                 f"💧 Humidity: {humidity}%\n"
                 f"☁ Cloud: {cloud}%\n"
                 f"📌 Condition: {condition}"
        )
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong!\n{e}")

# Tkinter window
root = tk.Tk()
root.title("Weather App 🌦")
root.geometry("400x300")
root.config(bg="#e6f2ff")

# Title
title_label = tk.Label(root, text="🌍 Weather App", font=("Arial", 16, "bold"), bg="#e6f2ff", fg="blue")
title_label.pack(pady=10)

# City input
city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=5)

# Button
get_btn = tk.Button(root, text="Get Weather", font=("Arial", 12, "bold"), bg="lightblue", command=get_weather)
get_btn.pack(pady=5)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#e6f2ff", justify="left")
result_label.pack(pady=10)

# Run loop
root.mainloop()
