# Importing the Library
import pandas as pd
from flask import request, Flask, jsonify
import requests
import json

# Initialize Flask application
app = Flask(__name__)

# MLflow server endpoint
# Define the URL and headers
host = '127.0.0.1'
port = '5021'  # Ensure this is the correct port where MLflow server is running
mlflow_server_url = f'http://{host}:{port}/invocations'
headers = {'Content-Type': 'application/json'}

@app.route('/diabetesPrediction', methods=['POST'])
def diabetesPrediction():
    try:
        # Get JSON data from the request
        data = request.json
        
        # Extracting the values and formatting them into the desired MLFlow structure
        data = data['data'][0]
        formatted_data = {
            'instances': [
                [
                    data['Pregnancies'],
                    data['Glucose'],
                    data['BloodPressure'],
                    data['SkinThickness'],
                    data['Insulin'],
                    data['BMI'],
                    data['DiabetesPedigreeFunction'],
                    data['Age']
                ]
            ]
        }

        # Convert the input data to JSON format
        formatted_data_json = json.dumps(formatted_data)

        # Make the POST request
        response = requests.post(url=mlflow_server_url, headers=headers, data=formatted_data_json)
        
        # Check if the response is successful
        if response.status_code != 200:
            return jsonify({'error': 'Failed to get prediction from MLflow server'}), response.status_code
        
        # Parse response JSON
        response_json = response.json()

        # Extract the prediction value
        prediction_value = response_json.get("predictions", [None])[0]

        # Map prediction values to messages
        if prediction_value == 0:
            result_message = "Negative"
        elif prediction_value == 1:
            result_message = "Positive"
        else:
            result_message = "Unknown"  # Handle unexpected values if necessary

        # Format the result into the desired structure
        formatted_result = {
            "Your diabetes test results are:": result_message
        }

        return jsonify(formatted_result)

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Run the Flask application
app.run(debug=True, host="0.0.0.0", port=5010)
