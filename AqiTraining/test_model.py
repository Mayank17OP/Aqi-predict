import pickle
import pandas as pd

# Load the trained model
model = pickle.load(open("aqi_model.pkl", "rb"))

# Example Input (Temp, Humidity, Wind Speed, Last AQI)
# Make sure to pass a DataFrame with the same columns as the trained model
test_input = pd.DataFrame([[18, 65, 3.2, 400]], columns=['temp', 'humidity', 'wind_speed', 'aqi'])

# Predict
predicted_aqi = model.predict(test_input)[0]
print(f"🔮 Predicted AQI: {predicted_aqi}")

