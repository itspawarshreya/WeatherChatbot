import requests
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image


# OpenWeatherMap API key
API_KEY = "6778964c3d3c001c28ee4ad199338518"

# Function to get weather information
def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            weather_desc = data['weather'][0]['description']
            temperature = data['main']['temp']
            temp_celsius = round(temperature - 273.15, 2)
            return f"The weather in {city} is {weather_desc}. The temperature is {temp_celsius}°C."
        else:
            return "Could not retrieve weather information."
    except Exception as e:
        print(e)
        return "An error occurred while retrieving weather information."


# Function to handle user input and display weather information
def process_input():
    city = entry.get()
    if city:
        response = get_weather(city)
        messagebox.showinfo("Weather Information", response)
    else:
        messagebox.showwarning("Warning", "Please enter a city name.")

# Create the main window
window = tk.Tk()
window.title("Weather Chatbot")

# Set window size and position
window.geometry("400x300")
window.resizable(False, False)
window.configure(background="#F0F0F0")

# Load and display background image
background_image = Image.open("WC image.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create and pack the label
label = tk.Label(window, text="Enter a city name:", font=("Arial", 16), bg="#F0F0F0")
label.pack(pady=20)

# Create and pack the entry field
entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)

# Create and pack the button
button = tk.Button(window, text="Get Weather", command=process_input, font=("Arial", 14), bg="#4CAF50", fg="white")
button.pack(pady=10)

# Run the main window loop
window.mainloop()
