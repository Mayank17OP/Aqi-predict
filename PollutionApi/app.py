from flask import Flask, jsonify, request
import pickle
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Specify the absolute path to the model file (update with your path)


# Load the trained model
model = pickle.load(open('../ApiTraining/aqi_model.pkl', 'rb'))


# Define a route for AQI prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the POST request (in JSON format)
    data = request.get_json()

    # Extract features from the request
    try:
        temp = data['temp']
        humidity = data['humidity']
        wind_speed = data['wind_speed']
        last_aqi = data['last_aqi']
    except KeyError:
        return jsonify({"error": "Missing required data"}), 400

    # Prepare the input data in the same format as training data
    input_data = np.array([[temp, humidity, wind_speed, last_aqi]])

    # Make prediction
    predicted_aqi = model.predict(input_data)[0]

    # Return the prediction as JSON
    return jsonify({"predicted_aqi": predicted_aqi})


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
