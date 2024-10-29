import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Load dataset from CSV file
dataset = pd.read_csv("weather_data.csv")

# Extract features and target
X = dataset[['Temperature', 'Humidity', 'Wind_Speed', 'Precipitation']].values
y = dataset['Weather_Type'].values

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Function to predict weather type
def predict_weather():
    try:
        temperature_str = temp_entry.get()
        if not temperature_str:
            raise ValueError("Temperature field cannot be empty")
        temperature = int(temperature_str)
        if not 10 <= temperature <= 35:
            raise ValueError("Temperature must be an integer between 10 and 35")
        
        humidity_str = humidity_entry.get()
        if not humidity_str:
            raise ValueError("Humidity field cannot be empty")
        humidity = int(humidity_str)
        if not 40 <= humidity <= 90:
            raise ValueError("Humidity must be an integer between 40 and 90")
        
        wind_speed_str = wind_entry.get()
        if not wind_speed_str:
            raise ValueError("Wind speed field cannot be empty")
        wind_speed = int(wind_speed_str)
        if not 0 <= wind_speed <= 30:
            raise ValueError("Wind speed must be an integer between 0 and 30")
        
        precip_str = precip_entry.get()
        if not precip_str:
            raise ValueError("Precipitation field cannot be empty")
        precipitation = int(precip_str)
        if not 0 <= precipitation <= 5:
            raise ValueError("Precipitation must be an integer between 0 and 5")
        
        # Predicting weather type
        weather_type = clf.predict([[temperature, humidity, wind_speed, precipitation]])
        messagebox.showinfo("Weather Prediction", f"Predicted Weather: {weather_type[0]}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# GUI
root = tk.Tk()
root.title("Weather Predictor By Sridhar")
root.configure(background='black')  # Set background to black

# Labels and Entries for user input
temp_label = ttk.Label(root, text="Temperature (°C) [10-35]:", background='black', foreground='yellow', font=("Times", 24, "bold italic"))
temp_label.grid(row=0, column=0, padx=5, pady=5)
temp_entry = ttk.Entry(root, font=("Times", 24, "bold italic"))
temp_entry.grid(row=0, column=1, padx=5, pady=5)

humidity_label = ttk.Label(root, text="Humidity (%) [40-90]:", background='black', foreground='yellow', font=("Times", 24, "bold italic"))
humidity_label.grid(row=1, column=0, padx=5, pady=5)
humidity_entry = ttk.Entry(root, font=("Times", 24, "bold italic"))
humidity_entry.grid(row=1, column=1, padx=5, pady=5)

wind_label = ttk.Label(root, text="Wind Speed (km/h) [0-30]:", background='black', foreground='yellow', font=("Times", 24, "bold italic"))
wind_label.grid(row=2, column=0, padx=5, pady=5)
wind_entry = ttk.Entry(root, font=("Times", 24, "bold italic"))
wind_entry.grid(row=2, column=1, padx=5, pady=5)

precip_label = ttk.Label(root, text="Precipitation (mm):", background='black', foreground='yellow', font=("Times", 24, "bold italic"))
precip_label.grid(row=3, column=0, padx=5, pady=5)
precip_entry = ttk.Entry(root, font=("Times", 24, "bold italic"))  # Entry field for precipitation
precip_entry.grid(row=3, column=1, padx=5, pady=5)

# Button to predict weather
predict_button = ttk.Button(root, text="Predict Weather", command=predict_weather)
predict_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
predict_button.config(width=20)

root.mainloop()
