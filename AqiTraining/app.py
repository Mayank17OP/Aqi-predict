import pickle
from flask import Flask, jsonify, request
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model (adjust the path to your model if needed)
model = pickle.load(open('aqi_model.pkl', 'rb'))

# Home route to check if Flask is working
@app.route('/')
def home():
    return "Flask is running!"

# Route for AQI prediction (only accepts POST requests)
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the POST request (expects JSON)
    data = request.get_json()

    # Extract features from the data
    try:
        temp = data['temp']
        humidity = data['humidity']
        wind_speed = data['wind_speed']
        last_aqi = data['last_aqi']
    except KeyError:
        return jsonify({"error": "Missing required data"}), 400

    # Prepare input data in the same format as the model's training data
    input_data = np.array([[temp, humidity, wind_speed, last_aqi]])

    # Use the model to predict AQI
    predicted_aqi = model.predict(input_data)[0]

    # Return the predicted AQI as a JSON response
    return jsonify({"predicted_aqi": predicted_aqi})

# Route to handle favicon requests (optional)
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Empty response to avoid favicon error

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)


