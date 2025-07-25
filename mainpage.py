import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

# Function to fetch weather data
def get_weather(city):
    api_key = '2a6bba17e6463fbcddd3b47c9f96711b' 
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

# Function to display weather information
def show_weather():
    city1 = city_entry1.get()
    city2 = city_entry2.get()
    
    weather_data1 = get_weather(city1)
    weather_data2 = get_weather(city2)
    
    if weather_data1.get('cod') != 200:
        messagebox.showerror('Error', f'City {city1} not found!')
        return
    if weather_data2.get('cod') != 200:
        messagebox.showerror('Error', f'City {city2} not found!')
        return
    print(weather_data1)
    print(weather_data2)
    # additional data for city 1
    visibility1 = weather_data1.get('visibility', 'N/A')
    pressure1 = weather_data1['main']['pressure']
    temp_min1 = weather_data1['main']['temp_min']
    temp_max1 = weather_data1['main']['temp_max']
    sunrise1 = datetime.utcfromtimestamp(weather_data1['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
    sunset1 = datetime.utcfromtimestamp(weather_data1['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
    cloudiness1 = weather_data1['clouds']['all']
    last_update1 = datetime.utcfromtimestamp(weather_data1['dt']).strftime('%Y-%m-%d %H:%M:%S')

    # additional data for city 2
    visibility2 = weather_data2.get('visibility', 'N/A')
    pressure2 = weather_data2['main']['pressure']
    temp_min2 = weather_data2['main']['temp_min']
    temp_max2 = weather_data2['main']['temp_max']
    sunrise2 = datetime.utcfromtimestamp(weather_data2['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
    sunset2 = datetime.utcfromtimestamp(weather_data2['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
    cloudiness2 = weather_data2['clouds']['all']
    last_update2 = datetime.utcfromtimestamp(weather_data2['dt']).strftime('%Y-%m-%d %H:%M:%S')

    # result labels
    result_label1.config(text=f"City: {city1}\n"
                             f"Temperature: {weather_data1['main']['temp']}°C\n"
                             f"Weather: {weather_data1['weather'][0]['description']}\n"
                             f"Humidity: {weather_data1['main']['humidity']}%\n"
                             f"Wind Speed: {weather_data1['wind']['speed']} m/s\n"
                             f"Visibility: {visibility1} meters\n"
                             f"Pressure: {pressure1} hPa\n"
                             f"Min Temp: {temp_min1}°C\n"
                             f"Max Temp: {temp_max1}°C\n"
                             f"Cloudiness: {cloudiness1}%\n"
                             f"Sunrise: {sunrise1}\n"
                             f"Sunset: {sunset1}\n"
                             f"Last Update: {last_update1}")

    result_label2.config(text=f"City: {city2}\n"
                             f"Temperature: {weather_data2['main']['temp']}°C\n"
                             f"Weather: {weather_data2['weather'][0]['description']}\n"
                             f"Humidity: {weather_data2['main']['humidity']}%\n"
                             f"Wind Speed: {weather_data2['wind']['speed']} m/s\n"
                             f"Visibility: {visibility2} meters\n"
                             f"Pressure: {pressure2} hPa\n"
                             f"Min Temp: {temp_min2}°C\n"
                             f"Max Temp: {temp_max2}°C\n"
                             f"Cloudiness: {cloudiness2}%\n"
                             f"Sunrise: {sunrise2}\n"
                             f"Sunset: {sunset2}\n"
                             f"Last Update: {last_update2}")

# Set up the main application window
app = tk.Tk()
app.title("Weather App")

# City input for first city
tk.Label(app, text="Enter first city name:", font=("Times New Roman", 20, "bold")).pack(pady=10)
city_entry1 = tk.Entry(app)
city_entry1.pack(pady=5)

# City input for second city
tk.Label(app, text="Enter second city name:", font=("Times New Roman", 20, "bold")).pack(pady=10)
city_entry2 = tk.Entry(app)
city_entry2.pack(pady=5)

# Show weather button
tk.Button(app, text="Show Weather", font=("Times New Roman", 10, "bold"), command=show_weather).pack(pady=10)

# Result display for first city
result_label1 = tk.Label(app, text="", font=('bold', 12), justify='left')
result_label1.pack(pady=10)

# Result display for second city
result_label2 = tk.Label(app, text="", font=('bold', 12), justify='left')
result_label2.pack(pady=10)
print()

# Start the application
app.mainloop()
