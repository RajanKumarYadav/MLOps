from src.MLOPs_project_auto_template_exception_and_logging.logger import logging
from src.MLOPs_project_auto_template_exception_and_logging.exception import CustomException

import sys

# Importing the Library
import pandas as pd
from flask import request, Flask, jsonify
import requests
import json

# Initialize Flask application
app = Flask(__name__)


@app.route('/diabetesPrediction', methods=['POST'])
def diabetesPrediction():

    try:
        # Get JSON data from the request
        data = request.json

        # var =10
        # test = var / 0
        
        # Use of Logger 
        logging.info("The Flask Application has started")
        return data

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)

# Run the Flask application
app.run(debug=True, host="0.0.0.0", port=5010)
