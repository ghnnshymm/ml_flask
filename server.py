from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow import keras

app = Flask(__name__)

# Load the pre-trained model
model = keras.models.load_model("churn_model.h5")

def preprocess_data(input_data):
    # Assuming the JSON data contains a list of features
    features = input_data.get("features", [])
    processed_data = np.array(features) #performs preprocessing if necessary

    return processed_data

def postprocess_predictions(predictions):
    return predictions.tolist()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the POST request
        data = request.get_json()

        # Preprocess the input data to match the model's requirements
        input_data = preprocess_data(data)

        # Make predictions using the loaded model
        predictions = model.predict(np.array([input_data]))

        # You can format the predictions
        formatted_predictions = postprocess_predictions(predictions)

        return jsonify({"predictions": formatted_predictions})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.debug = True
    app.run()
