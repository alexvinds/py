import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

# Загрузка модели
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def root():
    return 'Модель работает!'

@app.route('/predict', methods=['POST'])
def predict():
    # Ожидаем json с массивом признаков, например: {"input": [[0.1, 0.2, ...]]}
    data = request.get_json()
    
    if not data or 'input' not in data:
        return jsonify({'error': 'Пожалуйста, передайте {"input": [[...], ...]}'}), 400
    
    X = np.array(data['input'])
    preds = model.predict(X)
    return jsonify({'prediction': preds.tolist()})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)