from flask import Flask, jsonify, request, render_template
import os
import pandas as pd
from transformers import BertTokenizer
import torch.nn as nn
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Directory where models and CSV files are stored
MODEL_DIR = "../models"
CSV_DIR = "../CSV"

# Function to list available models
def list_models():
    return [f for f in os.listdir(MODEL_DIR) if f.endswith(".h5")]

# Function to load a specific model
def load_selected_model(model_name):
    model_path = os.path.join(MODEL_DIR, model_name)
    if os.path.exists(model_path):
        return load_model(model_path)
    else:
        raise FileNotFoundError(f"Model {model_name} not found in {MODEL_DIR}")

# Function to get the corresponding CSV file for a model
def get_csv_file(model_name):
    csv_name = f"coin_{model_name.split('_')[0]}.csv"
    csv_path = os.path.join(CSV_DIR, csv_name)
    if os.path.exists(csv_path):
        return csv_path
    else:
        raise FileNotFoundError(f"CSV file {csv_name} not found in {CSV_DIR}")\

# Endpoint to fetch available models
@app.route('/models', methods=['GET'])
def get_models():
    models = list_models()
    return jsonify(models)

# Endpoint to fetch data and make predictions
@app.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    model_name = data.get("model_name")
    timeframe = data.get("timeframe", "months")

    if not model_name:
        return jsonify({"error": "Model name is required"}), 400

    try:
        # Load the selected model and its associated CSV file
        model = load_selected_model(model_name)
        csv_path = get_csv_file(model_name)
        df = pd.read_csv(csv_path)

        # Prepare data for prediction
        scaler = MinMaxScaler(feature_range=(0, 1))
        df['scaled_price'] = scaler.fit_transform(df[['Close']].values)

        # Get the input sequences for prediction
        sequence_length = model.input_shape[1]
        sequences = []
        for i in range(len(df) - sequence_length):
            sequences.append(df['scaled_price'].values[i:i + sequence_length])
        sequences = np.array(sequences)

        # Predict prices
        predictions_scaled = model.predict(sequences)
        predictions = scaler.inverse_transform(predictions_scaled)

        # Prepare response data
        actual_prices = df['Close'].values[sequence_length:]
        dates = df['Date'].values[sequence_length:]
        response = {
            "prices": {
                "dates": dates.tolist() if timeframe == "months" else dates[-365:].tolist(),
                "actual": actual_prices.tolist() if timeframe == "months" else actual_prices[-365:].tolist(),
                "predicted": predictions.flatten().tolist() if timeframe == "months" else predictions.flatten()[-365:].tolist(),
            }
        }
        return jsonify(response)

    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": f"Error during prediction: {str(e)}"}), 500

# Endpoint to fetch the next predicted price
@app.route('/next_price', methods=['POST'])
def next_price():
    data = request.get_json()
    model_name = data.get("model_name")

    if not model_name:
        return jsonify({"error": "Model name is required"}), 400

    try:
        # Load the selected model
        model = load_selected_model(model_name)

        # Load the associated CSV file
        csv_path = get_csv_file(model_name)
        df = pd.read_csv(csv_path)

        # Prepare data for prediction
        scaler = MinMaxScaler(feature_range=(0, 1))
        df['scaled_price'] = scaler.fit_transform(df[['Close']].values)

        # Get the last sequence of data
        sequence_length = model.input_shape[1]
        last_sequence = df['scaled_price'].values[-sequence_length:].reshape(1, -1, 1)

        # Predict the next price
        next_price_scaled = model.predict(last_sequence)
        next_price = scaler.inverse_transform(next_price_scaled)[0][0]  # Rescale to original price range

        # Convert to standard Python float for JSON serialization
        next_price = float(next_price)

        # Return the next predicted price
        return jsonify({"next_price": next_price})
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": f"Error during prediction: {str(e)}"}), 500
    
# Homepage
@app.route('/')
def home():
    return render_template('index.html', models=list_models())

# Explicit route for Crypto Price Prediction
@app.route('/crypto-price-prediction')
def crypto_price_prediction():
    models = list_models()
    return render_template('index.html', models=models)

# Sentiment Analysis route
@app.route('/sentiment-analysis')
def sentiment_analysis():
    return render_template('sentiment_analysis.html')

if __name__ == '__main__':
    app.run(debug=True)
