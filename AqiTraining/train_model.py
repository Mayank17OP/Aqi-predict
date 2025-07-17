import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# ✅ Load Data
df = pd.read_csv("aqi_data.csv", names=["timestamp", "aqi", "temp", "humidity", "wind_speed"])

# ✅ Create Prediction Target
df["future_aqi"] = df["aqi"].shift(-1)  # Next day's AQI
df.dropna(inplace=True)

# ✅ Select Features & Target
X = df[['temp', 'humidity', 'wind_speed', 'aqi']]
y = df['future_aqi']

# ✅ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train Model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# ✅ Save Model
pickle.dump(model, open("aqi_model.pkl", "wb"))

print("🎯 Model Trained & Saved as aqi_model.pkl!")
