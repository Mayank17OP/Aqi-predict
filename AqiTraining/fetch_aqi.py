import requests
import csv
from datetime import datetime

# ✅ Step 1: Replace API Key
API_KEY = "YOUR_WAQI_API_KEY"  # Apni WAQI API key daalo
CITY = "delhi"
API_URL = f"https://api.waqi.info/feed/delhi/?token=1d71fe9893fd558440b8fbb138f9a983b673c41c"

# ✅ Step 2: Fetch API Data
response = requests.get(API_URL)
data = response.json()  # Convert response to dictionary

print("🔹 API Response:", data)  # Debug print

# ✅ Step 3: Extract AQI Data
if "data" in data and isinstance(data["data"], dict):
    aqi = data["data"].get("aqi", "No AQI Data")
    temp = 18  # Dummy Data
    humidity = 65  # Dummy Data
    wind_speed = 3.2  # Dummy Data

    # ✅ Step 4: Save to CSV
    with open("aqi_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), aqi, temp, humidity, wind_speed])

    print(f"✅ Saved AQI Data: {aqi}, Temp: {temp}, Humidity: {humidity}, Wind Speed: {wind_speed}")
else:
    print("⚠️ API Error:", data)
