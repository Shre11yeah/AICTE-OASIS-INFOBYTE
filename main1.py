import tkinter as tk
from tkinter import messagebox

# Mock function to get weather data
def get_weather_data(location):
    # Replace this function with one that fetches real weather data
    weather_data = {
        "location": location,
        "current_conditions": "Sunny",
        "temperature": "25°C",
        "hourly_forecast": ["12 PM: Sunny", "1 PM: Partly Cloudy", "2 PM: Cloudy"],
        "daily_forecast": ["Monday: Sunny", "Tuesday: Partly Cloudy", "Wednesday: Rainy"],
        "wind_speed": "10 km/h",
    }
    return weather_data

def fetch_weather():
    location = location_entry.get()
    if location:
        weather_data = get_weather_data(location)
        display_weather(weather_data)
    else:
        messagebox.showerror("Error", "Please enter a location")

def display_weather(weather_data):
    location_label.config(text=f"Location: {weather_data['location']}", font=("Helvetica", 14, "bold"))
    current_conditions_label.config(text=f"Current Conditions: {weather_data['current_conditions']}", font=("Helvetica", 12))
    temperature_label.config(text=f"Temperature: {weather_data['temperature']}", font=("Helvetica", 12))
    hourly_forecast_label.config(text="Hourly Forecast:\n" + "\n".join(weather_data['hourly_forecast']), font=("Helvetica", 12))
    daily_forecast_label.config(text="Daily Forecast:\n" + "\n".join(weather_data['daily_forecast']), font=("Helvetica", 12))
    wind_speed_label.config(text=f"Wind Speed: {weather_data['wind_speed']}", font=("Helvetica", 12))

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")

# Create and place widgets
location_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
location_label.pack(pady=10)

current_conditions_label = tk.Label(root, text="", font=("Helvetica", 12))
current_conditions_label.pack(pady=5)

temperature_label = tk.Label(root, text="", font=("Helvetica", 12))
temperature_label.pack(pady=5)

hourly_forecast_label = tk.Label(root, text="", font=("Helvetica", 12))
hourly_forecast_label.pack(pady=5)

daily_forecast_label = tk.Label(root, text="", font=("Helvetica", 12))
daily_forecast_label.pack(pady=5)

wind_speed_label = tk.Label(root, text="", font=("Helvetica", 12))
wind_speed_label.pack(pady=5)

location_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
location_entry.pack(pady=10)

fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white")
fetch_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
